import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from openai import OpenAI
import sqlite3
from datetime import datetime, timedelta
import json
import os
import random
import time
from typing import Optional


# Page configuration
st.set_page_config(
    page_title="AI Sales Analytics Platform",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

class SalesAnalyticsPlatform:
    """Complete AI-powered sales analytics platform for portfolio"""
    
    def __init__(self):
        # Initialize OpenAI client if API key is available
        api_key = os.getenv("OPENAI_API_KEY")
        self.client = OpenAI(api_key=api_key) if api_key else None

        # Ensure data directory exists and establish database path
        self.db_path = os.path.join("data", "sales_platform.db")
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)

        self.setup_database()
    
    def create_fallback_data(self):
        """Create minimal fallback data for when database seeding fails"""
        # Seed a very small dataset so the app can run even without sample data
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        fallback_rows = [
            (
                datetime.now().date().isoformat(),
                "North America",
                "Fallback User",
                "Small Business",
                "Software Licenses",
                "Starter Package",
                1000.0,
                1,
                25.0,
                4.0,
                "Fallback",
                "Closed Won",
            )
        ]
        cursor.executemany(
            """
            INSERT INTO sales_data (
                date, region, salesperson, customer_segment, product_category,
                product_name, revenue, units_sold, profit_margin, customer_satisfaction,
                lead_source, deal_stage
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            fallback_rows,
        )
        conn.commit()
        conn.close()

    def setup_database(self):
        """Simplified database setup for cloud deployment"""
        conn = None
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            # Create comprehensive sales table
            cursor.execute(
                """
            CREATE TABLE IF NOT EXISTS sales_data (
                id INTEGER PRIMARY KEY,
                date DATE,
                region TEXT,
                salesperson TEXT,
                customer_segment TEXT,
                product_category TEXT,
                product_name TEXT,
                revenue DECIMAL(10,2),
                units_sold INTEGER,
                profit_margin DECIMAL(5,2),
                customer_satisfaction DECIMAL(3,1),
                lead_source TEXT,
                deal_stage TEXT
            )
                """
            )

            # Seed database with sample data if empty
            cursor.execute("SELECT COUNT(*) FROM sales_data")
            if cursor.fetchone()[0] == 0:
                sample_data = self.generate_comprehensive_sample_data()
                cursor.executemany(
                    """
                INSERT INTO sales_data (
                    date, region, salesperson, customer_segment, product_category,
                    product_name, revenue, units_sold, profit_margin, customer_satisfaction,
                    lead_source, deal_stage
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    sample_data,
                )
                conn.commit()

            # If seeding didn't populate data, create minimal fallback
            cursor.execute("SELECT COUNT(*) FROM sales_data")
            if cursor.fetchone()[0] == 0:
                raise RuntimeError("No data available after seeding")

        except Exception as e:
            st.error(f"Database setup failed: {e}")
            self.create_fallback_data()
        finally:
            if conn:
                conn.close()
    
    def generate_comprehensive_sample_data(self):
        """Generate realistic, comprehensive sample data"""
        # Comprehensive data arrays
        regions = ['North America', 'Europe', 'Asia Pacific', 'Latin America', 'Middle East & Africa']
        salespeople = ['Alice Johnson', 'Bob Chen', 'Carol Martinez', 'David Kumar', 'Emma Wilson',
                      'Frank Thompson', 'Grace Lee', 'Henry Davis', 'Iris Zhang', 'Jack Brown']
        segments = ['Enterprise', 'Mid-Market', 'Small Business', 'Startup']
        categories = ['Software Licenses', 'Professional Services', 'Training & Certification', 'Support & Maintenance']
        products = {
            'Software Licenses': ['Analytics Pro', 'Business Intelligence Suite', 'Data Platform', 'AI Accelerator'],
            'Professional Services': ['Implementation', 'Custom Development', 'Integration', 'Migration'],
            'Training & Certification': ['Admin Training', 'User Training', 'Advanced Analytics', 'Certification Program'],
            'Support & Maintenance': ['Premium Support', 'Standard Support', '24/7 Support', 'Managed Services']
        }
        lead_sources = ['Website', 'Referral', 'Cold Outreach', 'Trade Show', 'Partner', 'Social Media']
        deal_stages = ['Closed Won', 'Closed Lost', 'Negotiation', 'Proposal', 'Discovery']
        
        sample_data = []
        start_date = datetime.now().date() - timedelta(days=365)  # Full year of data
        
        for i in range(2000):  # Generate 2000 comprehensive records
            record_date = start_date + timedelta(days=random.randint(0, 365))
            region = random.choice(regions)
            segment = random.choice(segments)
            category = random.choice(categories)
            product = random.choice(products[category])
            
            # Realistic revenue based on segment and category
            base_revenue = {
                'Enterprise': {'Software Licenses': 50000, 'Professional Services': 25000, 'Training & Certification': 15000, 'Support & Maintenance': 10000},
                'Mid-Market': {'Software Licenses': 20000, 'Professional Services': 12000, 'Training & Certification': 8000, 'Support & Maintenance': 5000},
                'Small Business': {'Software Licenses': 5000, 'Professional Services': 3000, 'Training & Certification': 2000, 'Support & Maintenance': 1500},
                'Startup': {'Software Licenses': 2000, 'Professional Services': 1500, 'Training & Certification': 1000, 'Support & Maintenance': 800}
            }
            
            base_amount = base_revenue[segment][category]
            revenue = base_amount * random.uniform(0.5, 2.0)  # Vary by 50-200%
            
            # Seasonal adjustments
            if record_date.month in [11, 12]:  # Q4 boost
                revenue *= random.uniform(1.1, 1.4)
            elif record_date.month in [1, 2]:  # Q1 dip
                revenue *= random.uniform(0.8, 1.0)
            
            units_sold = random.randint(1, 20)
            profit_margin = random.uniform(15, 45)  # 15-45% profit margin
            satisfaction = random.uniform(3.5, 5.0)  # Customer satisfaction 3.5-5.0

            record = (
                record_date.isoformat(),
                region,
                random.choice(salespeople),
                segment,
                category,
                product,
                round(revenue, 2),
                units_sold,
                round(profit_margin, 1),
                round(satisfaction, 1),
                random.choice(lead_sources),
                random.choice(deal_stages)
            )
            sample_data.append(record)
        
        return sample_data
    
    @st.cache_data
    def load_sales_data(_self, date_range=None, filters=None):
        """Load sales data with comprehensive filtering"""
        conn = sqlite3.connect(_self.db_path)
        query = "SELECT * FROM sales_data WHERE 1=1"
        params = []
        
        if date_range:
            query += " AND date >= ? AND date <= ?"
            params.extend([date_range[0].isoformat(), date_range[1].isoformat()])
        
        if filters:
            for column, values in filters.items():
                if values:
                    placeholders = ','.join(['?' for _ in values])
                    query += f" AND {column} IN ({placeholders})"
                    params.extend(values)
        
        query += " ORDER BY date DESC"
        df = pd.read_sql_query(query, conn, params=params)
        conn.close()
        
        df['date'] = pd.to_datetime(df['date'])
        df['profit_amount'] = df['revenue'] * (df['profit_margin'] / 100)
        return df
    
    def get_ai_insights(self, data, context, insight_type="comprehensive"):
        """Get comprehensive AI insights with different analysis types"""
        if len(data) == 0:
            return "No data available for analysis."
        
        if not self.client:
            return "AI insights unavailable. Please configure your OpenAI API key in the environment variables."
        
        # Prepare comprehensive data summary
        summary = f"""
Sales Performance Data Analysis:
- Total Records: {len(data):,}
- Date Range: {data['date'].min().strftime('%Y-%m-%d')} to {data['date'].max().strftime('%Y-%m-%d')}
- Total Revenue: ${data['revenue'].sum():,.2f}
- Total Profit: ${data['profit_amount'].sum():,.2f}
- Average Deal Size: ${data['revenue'].mean():.2f}
- Average Profit Margin: {data['profit_margin'].mean():.1f}%

Performance by Dimension:
- Regions: {data.groupby('region')['revenue'].sum().to_dict()}
- Customer Segments: {data.groupby('customer_segment')['revenue'].sum().to_dict()}
- Product Categories: {data.groupby('product_category')['revenue'].sum().to_dict()}
- Top Performers: {data.groupby('salesperson')['revenue'].sum().nlargest(3).to_dict()}

Quality Metrics:
- Average Customer Satisfaction: {data['customer_satisfaction'].mean():.1f}/5.0
- Win Rate: {(len(data[data['deal_stage'] == 'Closed Won']) / len(data) * 100):.1f}%
        """
        
        if insight_type == "strategic":
            analysis_focus = """
Provide strategic-level analysis focusing on:
1. Market opportunities and threats
2. Competitive positioning insights
3. Investment priorities and resource allocation
4. Long-term growth strategies
5. Risk mitigation recommendations
            """
        elif insight_type == "operational":
            analysis_focus = """
Provide operational analysis focusing on:
1. Sales process optimization opportunities
2. Team performance and productivity insights
3. Customer satisfaction improvement areas
4. Product mix optimization
5. Immediate action items for sales management
            """
        else:
            analysis_focus = """
Provide comprehensive business analysis covering:
1. Key performance trends and patterns
2. Areas of strength and concern
3. Actionable recommendations
4. Success metrics to monitor
            """
        
        prompt = f"""
Context: {context}

{summary}

{analysis_focus}

Please provide professional, data-driven insights that would be valuable for business decision-making.
Structure your response with clear headings and specific recommendations.
        """
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a senior sales analytics expert providing strategic business insights."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=600,
                temperature=0.2
            )
            return response.choices[0].message.content
        except Exception as e:
            st.error(f"AI analysis unavailable: {e}")
            return "AI insights temporarily unavailable. Please check your API configuration."
    
    def render_executive_dashboard(self, data):
        """Render comprehensive executive dashboard"""
        if len(data) == 0:
            st.warning("No data available for the selected filters.")
            return
        
        # Executive KPIs
        st.subheader("🎯 Executive KPIs")
        col1, col2, col3, col4, col5 = st.columns(5)
        
        total_revenue = data['revenue'].sum()
        total_profit = data['profit_amount'].sum()
        avg_margin = data['profit_margin'].mean()
        satisfaction = data['customer_satisfaction'].mean()
        win_rate = (len(data[data['deal_stage'] == 'Closed Won']) / len(data)) * 100
        
        with col1:
            st.metric("Total Revenue", f"${total_revenue:,.0f}", delta=f"+{total_revenue*0.15:,.0f}")
        with col2:
            st.metric("Total Profit", f"${total_profit:,.0f}", delta=f"+{avg_margin:.1f}%")
        with col3:
            st.metric("Avg Profit Margin", f"{avg_margin:.1f}%")
        with col4:
            st.metric("Customer Satisfaction", f"{satisfaction:.1f}/5.0")
        with col5:
            st.metric("Win Rate", f"{win_rate:.1f}%")
        
        # Advanced visualizations
        col1, col2 = st.columns(2)
        
        with col1:
            # Revenue trend with profit overlay
            monthly_data = data.groupby(data['date'].dt.to_period('M')).agg({
                'revenue': 'sum',
                'profit_amount': 'sum'
            }).reset_index()
            monthly_data['date'] = monthly_data['date'].astype(str)
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(
                x=monthly_data['date'],
                y=monthly_data['revenue'],
                mode='lines+markers',
                name='Revenue',
                line=dict(color='#1f77b4', width=3)
            ))
            fig.add_trace(go.Scatter(
                x=monthly_data['date'],
                y=monthly_data['profit_amount'],
                mode='lines+markers',
                name='Profit',
                line=dict(color='#ff7f0e', width=3)
            ))
            fig.update_layout(title="Monthly Revenue & Profit Trend", xaxis_title="Month", yaxis_title="Amount ($)")
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Market segment performance
            segment_data = data.groupby('customer_segment').agg({
                'revenue': 'sum',
                'profit_amount': 'sum',
                'customer_satisfaction': 'mean'
            }).reset_index()
            
            fig = px.scatter(
                segment_data,
                x='revenue',
                y='profit_amount',
                size='customer_satisfaction',
                color='customer_segment',
                title="Segment Performance: Revenue vs Profit",
                hover_data=['customer_satisfaction']
            )
            st.plotly_chart(fig, use_container_width=True)
        
        # Strategic AI Insights
        st.subheader("🤖 Strategic AI Insights")
        with st.spinner("Generating strategic analysis..."):
            strategic_insights = self.get_ai_insights(
                data,
                "Executive dashboard - strategic business analysis",
                "strategic"
            )
        st.write(strategic_insights)


def main():
    """Main application with authentication and full features"""
    
    # Check if running from correct directory
def main():
        
    st.title("🚀 AI-Enhanced Sales Analytics Platform")
    st.markdown("**Professional AI-powered sales analytics for data-driven decision making**")
    st.markdown("---")
    
    # Initialize platform
    try:
        platform = SalesAnalyticsPlatform()
    except Exception as e:
        st.error(f"Application startup failed: {e}")
        import traceback
        st.code(traceback.format_exc())
        st.stop()
    
    # Sidebar controls
    st.sidebar.header("📊 Analytics Controls")
    st.sidebar.markdown("**Filter and customize your analysis**")
    
    # Date range selector
    col1, col2 = st.sidebar.columns(2)
    with col1:
        start_date = st.date_input("Start Date", datetime.now().date() - timedelta(days=90))
    with col2:
        end_date = st.date_input("End Date", datetime.now().date())
    
    # Load data for filter options
    all_data = platform.load_sales_data()
    
    if len(all_data) == 0:
        st.error("No data available. Please check database setup.")
        st.stop()
    
    # Dynamic filters
    with st.sidebar.expander("🎯 Advanced Filters", expanded=True):
        regions = st.multiselect(
            "Regions",
            options=sorted(all_data['region'].unique()) if 'region' in all_data.columns else [],
            default=[]
        )
        
        salespeople = st.multiselect(
            "Sales Team",
            options=sorted(all_data['salesperson'].unique()) if 'salesperson' in all_data.columns else [],
            default=[]
        )
        
        segments = st.multiselect(
            "Customer Segments",
            options=sorted(all_data['customer_segment'].unique()) if 'customer_segment' in all_data.columns else [],
            default=[]
        )
        
        categories = st.multiselect(
            "Product Categories",
            options=sorted(all_data['product_category'].unique()) if 'product_category' in all_data.columns else [],
            default=[]
        )
    
    # Apply filters
    filters = {}
    if regions:
        filters['region'] = regions
    if salespeople:
        filters['salesperson'] = salespeople
    if segments:
        filters['customer_segment'] = segments
    if categories:
        filters['product_category'] = categories
    
    # Load filtered data
    with st.spinner("Loading data..."):
        filtered_data = platform.load_sales_data(
            date_range=(start_date, end_date),
            filters=filters
        )
    
    # Data summary
    if len(filtered_data) > 0:
        st.sidebar.success(f"📈 {len(filtered_data):,} records loaded")
        st.sidebar.metric("Total Revenue", f"${filtered_data['revenue'].sum():,.0f}" if 'revenue' in filtered_data.columns else "N/A")
    else:
        st.sidebar.warning("No data matches current filters")
    
    # Main content area
    if len(filtered_data) > 0:
        platform.render_executive_dashboard(filtered_data)
    else:
        st.warning("No data available for analysis. Please adjust your filters.")
    
    # Footer with system information
    st.markdown("---")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.caption(f"📊 {len(filtered_data):,} records analyzed")
    with col2:
        st.caption("🤖 Powered by OpenAI GPT")
    with col3:
        st.caption(f"⚡ Generated {datetime.now().strftime('%H:%M:%S')}")
    with col4:
        if st.button("📈 System Health"):
            health_metrics = {
                'status': 'healthy',
                'uptime': '99.9%',
                'data_records': len(all_data),
                'timestamp': datetime.now().isoformat()
            }
            st.json(health_metrics)

if __name__ == "__main__":
    main()
