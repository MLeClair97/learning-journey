# dashboard.py

import streamlit as st
import pandas as pd
import plotly.express as px
import openai
from sqlalchemy import create_engine
import os
from sqlalchemy.sql import text
from dotenv import load_dotenv
from openai import OpenAI


class DatabaseConnection:
    """Professional database connection class"""
    
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.engine = None
    
    def connect(self):
        """Create database engine"""
        try:
            self.engine = create_engine(self.connection_string)
            print("Database connection established")
            return True
        except Exception as e:
            print(f"Connection error: {e}")
            return False
    
    def execute_query(self, query, params=None):
        """Execute query and return DataFrame"""
        try:
            if params:
                df = pd.read_sql_query(text(query), self.engine, params=params)
            else:
                df = pd.read_sql_query(text(query), self.engine)
            return df
        except Exception as e:
            print(f"Query error: {e}")
            return None
    
    def close(self):
        """Close database connection"""
        if self.engine:
            self.engine.dispose()
            print("Database connection closed")


# ---------------- Page Setup ----------------
st.set_page_config(
    page_title="Business Analytics",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Business Analytics Dashboard")
st.markdown("---")


# ---------------- Database Query ----------------
@st.cache_data(ttl=300)
def load_data():
    """Load data from database"""
    # Load environment variables
    load_dotenv()
    
    # Get database URL from .env file
    database_url = os.getenv('DATABASE_URL')
    
    if not database_url:
        st.error("DATABASE_URL not found in environment variables")
        return pd.DataFrame()
    
    # Create database connection instance
    db = DatabaseConnection(database_url)
    
    # Connect and execute queries
    if db.connect():
        # Your practice query (adjusted for Chinook database)
        query = """
        SELECT 
            il.invoice_line_id,
            i.invoice_id,
            i.invoice_date,
            t.name as track_name,
            a.title as album_title,
            ar.name as artist_name,
            g.name as genre_name,
            il.unit_price,
            il.quantity,
            (il.unit_price * il.quantity) as revenue,
            c.country as region,
            1 as orders
        FROM invoice_line il 
        LEFT JOIN invoice i ON il.invoice_id = i.invoice_id
        LEFT JOIN customer c ON i.customer_id = c.customer_id
        INNER JOIN track t ON il.track_id = t.track_id
        INNER JOIN album a ON t.album_id = a.album_id
        INNER JOIN artist ar ON a.artist_id = ar.artist_id
        INNER JOIN genre g ON t.genre_id = g.genre_id
        WHERE i.invoice_date > '2010-01-01'
        ORDER BY i.invoice_date DESC;
        """
        
        df = db.execute_query(query)
        
        # Close connection
        db.close()
        
        if df is not None:
            print(f"Query successful! Total rows returned: {len(df)}")
            return df
        else:
            print("Query failed or returned no data")
            return pd.DataFrame()
    else:
        print("Failed to connect to database. Check your .env file and PostgreSQL setup.")
        return pd.DataFrame()


# ---------------- AI Analysis ----------------
def analyze_data_with_ai(df, prompt, analysis_type="insights"):
    """Analyze data using OpenAI with enhanced context and calculations"""
    try:
        # Check if OpenAI API key exists
        if "openai_api_key" not in st.secrets:
            return "OpenAI API key not found in Streamlit secrets."
        
        client = OpenAI(api_key=st.secrets["openai_api_key"])

        # Calculate additional metrics for deeper analysis
        df_analysis = df.copy()
        df_analysis['revenue_per_order'] = df_analysis['revenue'] / df_analysis['orders']
        df_analysis['revenue_share'] = (df_analysis['revenue'] / df_analysis['revenue'].sum()) * 100
        df_analysis['order_share'] = (df_analysis['orders'] / df_analysis['orders'].sum()) * 100
        
        # Sort by revenue
        df_analysis = df_analysis.sort_values('revenue', ascending=False)
        
        # Create rich context
        total_revenue = df_analysis['revenue'].sum()
        total_orders = df_analysis['orders'].sum()
        avg_order_value_global = total_revenue / total_orders
        
        top_5_regions = df_analysis.head(5)
        bottom_5_regions = df_analysis.tail(5)
        
        # Revenue concentration analysis
        top_3_revenue_share = df_analysis.head(3)['revenue_share'].sum()
        
        data_context = f"""
BUSINESS CONTEXT: This is music sales data from a digital music store (similar to iTunes/Spotify).

KEY METRICS:
- Total Revenue: ${total_revenue:,.2f}
- Total Orders: {total_orders:,}
- Global Average Order Value: ${avg_order_value_global:.2f}
- Revenue Concentration: Top 3 regions account for {top_3_revenue_share:.1f}% of total revenue

TOP 5 PERFORMING REGIONS:
{top_5_regions[['region', 'revenue', 'orders', 'revenue_per_order', 'revenue_share']].to_string(index=False)}

BOTTOM 5 PERFORMING REGIONS:
{bottom_5_regions[['region', 'revenue', 'orders', 'revenue_per_order', 'revenue_share']].to_string(index=False)}

COMPLETE DATA:
{df_analysis[['region', 'revenue', 'orders', 'revenue_per_order', 'revenue_share', 'order_share']].to_string(index=False)}
"""

        if analysis_type == "insights":
            system_prompt = """You are a senior business analyst specializing in digital music/entertainment markets. 
            Provide strategic insights that go beyond obvious observations. Focus on:
            
            1. MARKET OPPORTUNITIES: Which underperforming regions show potential? Why?
            2. REVENUE OPTIMIZATION: Where can average order values be improved?
            3. MARKET CONCENTRATION RISKS: Is revenue too concentrated in few regions?
            4. COMPETITIVE POSITIONING: What do regional differences suggest about market maturity?
            5. ACTIONABLE RECOMMENDATIONS: Specific strategies for growth
            
            Avoid stating obvious facts like "USA has the highest revenue." Instead, analyze WHY patterns exist and WHAT actions to take."""
            
        elif analysis_type == "strategic":
            system_prompt = """You are a strategic business consultant. Analyze this data from a CEO perspective:
            
            1. What are the biggest strategic risks in this revenue distribution?
            2. Which 3 regions represent the best expansion opportunities and why?
            3. What pricing or product strategies could increase revenue per order?
            4. How should marketing budgets be allocated across regions?
            5. What partnerships or local strategies might be needed?
            
            Think like McKinsey - provide framework-driven analysis with specific recommendations."""
            
        else:  # custom prompt
            system_prompt = "You are an expert business analyst. Provide deep, actionable insights beyond surface-level observations."

        full_prompt = f"{prompt}\n\n{data_context}"

        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": full_prompt}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"AI Error: {e}"


# ---------------- Load Data ----------------
data = load_data()

if data.empty:
    st.warning("No data found. Please check your database connection and query.")
    st.stop()

# Create region column if it doesn't exist
if 'region' not in data.columns:
    data['region'] = 'Unknown'

# Ensure required columns exist
required_columns = ['region', 'revenue', 'orders']
for col in required_columns:
    if col not in data.columns:
        if col == 'revenue':
            data['revenue'] = data.get('unit_price', 0) * data.get('quantity', 0)
        elif col == 'orders':
            data['orders'] = 1
        else:
            data[col] = 'Unknown'

# Group data by region for dashboard metrics
dashboard_data = data.groupby('region').agg({
    'revenue': 'sum',
    'orders': 'sum'
}).reset_index()


# ---------------- Sidebar Filters ----------------
st.sidebar.header("Dashboard Controls")

selected_regions = st.sidebar.multiselect(
    "Select Regions",
    options=dashboard_data['region'].unique(),
    default=dashboard_data['region'].unique()
)

filtered_data = dashboard_data[dashboard_data['region'].isin(selected_regions)]


# ---------------- Metrics ----------------
if not filtered_data.empty:
    col1, col2, col3 = st.columns(3)

    with col1:
        total_revenue = filtered_data['revenue'].sum()
        st.metric("Total Revenue", f"${total_revenue:,.2f}")

    with col2:
        total_orders = filtered_data['orders'].sum()
        st.metric("Total Orders", f"{total_orders:,}")

    with col3:
        avg_revenue = filtered_data['revenue'].mean()
        st.metric("Avg Revenue/Region", f"${avg_revenue:,.2f}")


    # ---------------- Chart ----------------
    st.subheader("Revenue by Region")
    fig = px.bar(filtered_data, x='region', y='revenue', title="Revenue Breakdown")
    st.plotly_chart(fig, use_container_width=True)


    # ---------------- AI Insights ----------------
    st.markdown("---")
    st.header("🤖 AI Insights")

    # Analysis type selector
    analysis_type = st.selectbox(
        "Choose Analysis Type:",
        ["insights", "strategic", "custom"],
        format_func=lambda x: {
            "insights": "🎯 Business Insights (Market opportunities, optimization)",
            "strategic": "📈 Strategic Analysis (CEO-level recommendations)", 
            "custom": "💬 Custom Question"
        }[x]
    )
    
    if analysis_type == "custom":
        user_question = st.text_input("Ask a specific business question about this data:")
        if st.button("Get AI Analysis") and user_question:
            with st.spinner("AI is analyzing..."):
                user_response = analyze_data_with_ai(filtered_data, user_question, "custom")
            st.write("**AI Analysis:**")
            st.write(user_response)
    else:
        if st.button("Generate Advanced AI Insights"):
            prompt = "Provide strategic business insights for this digital music sales data." if analysis_type == "strategic" else "What advanced business insights and opportunities do you see in this data?"
            
            with st.spinner("Generating advanced insights..."):
                ai_insights = analyze_data_with_ai(filtered_data, prompt, analysis_type)
            st.write(ai_insights)

    # Quick insight buttons
    st.subheader("Quick Analysis")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🎯 Market Opportunities"):
            with st.spinner("Analyzing market opportunities..."):
                insights = analyze_data_with_ai(filtered_data, "Identify the top 3 underperforming regions with the highest growth potential. What specific strategies would you recommend for each?", "strategic")
            st.write(insights)
    
    with col2:
        if st.button("💰 Revenue Optimization"):
            with st.spinner("Analyzing revenue optimization..."):
                insights = analyze_data_with_ai(filtered_data, "How can we increase revenue per order in each region? What pricing or product bundling strategies would work?", "strategic")
            st.write(insights)
    
    with col3:
        if st.button("⚠️ Risk Analysis"):
            with st.spinner("Analyzing business risks..."):
                insights = analyze_data_with_ai(filtered_data, "What are the main business risks in this revenue distribution? How should we diversify and mitigate these risks?", "strategic")
            st.write(insights)
else:
    st.warning("No data available for the selected regions.")

# ---------------- Debug Info ----------------
if st.sidebar.checkbox("Show Debug Info"):
    st.subheader("Debug Information")
    st.write("Raw data shape:", data.shape)
    st.write("Raw data columns:", list(data.columns))
    st.write("Dashboard data shape:", dashboard_data.shape)
    st.dataframe(data.head())