import openai
import pandas as pd
import os
import json
from database_connector import UniversalDatabaseAnalytics

class AIDataAnalyst:
    """AI-powered data analysis"""
    
    def __init__(self, api_key=None):
        # Set up OpenAI API (you'll need to set your API key)
        if api_key:
            openai.api_key = api_key
        else:
            openai.api_key = os.getenv('OPENAI_API_KEY')
        
        # Initialize database analytics
        self.db_analytics = UniversalDatabaseAnalytics()
        
        print("✅ AIDataAnalyst initialized")
        if not openai.api_key:
            print("⚠️  Warning: No OpenAI API key found. AI analysis will be simulated.")
    
    def analyze_dataframe_with_ai(self, df, question="What insights can you provide?"):
        """Analyze DataFrame with AI (or simulate if no API key)"""
        
        if not openai.api_key:
            # Simulate AI response for demo
            return self._simulate_ai_analysis(df, question)
        
        try:
            data_summary = {
                'shape': df.shape,
                'columns': list(df.columns),
                'sample_data': df.head(3).to_dict('records')
            }
            
            prompt = f"""
            Dataset: {data_summary['shape'][0]} rows, {data_summary['shape'][1]} columns
            Columns: {data_summary['columns']}
            Sample: {json.dumps(data_summary['sample_data'], indent=2, default=str)}
            
            Question: {question}
            
            Provide 3-4 key business insights in bullet points.
            """
            
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a senior data analyst."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=300,
                temperature=0.3
            )
            
            return response.choices[0].message.content
        
        except Exception as e:
            return f"AI Analysis Error: {e}"
    
    def _simulate_ai_analysis(self, df, question):
        """Simulate AI analysis when no API key is available"""
        
        insights = []
        
        # Basic statistical insights
        if len(df) > 0:
            insights.append(f"• Dataset contains {len(df)} records across {len(df.columns)} dimensions")
            
            # Find numeric columns
            numeric_cols = df.select_dtypes(include=['number']).columns
            if len(numeric_cols) > 0:
                for col in numeric_cols[:2]:  # Analyze first 2 numeric columns
                    avg_val = df[col].mean()
                    max_val = df[col].max()
                    insights.append(f"• {col}: Average is {avg_val:.1f}, Maximum is {max_val:.1f}")
            
            # Find categorical patterns
            categorical_cols = df.select_dtypes(include=['object']).columns
            if len(categorical_cols) > 0:
                col = categorical_cols[0]
                unique_count = df[col].nunique()
                most_common = df[col].value_counts().index[0]
                insights.append(f"• {col}: {unique_count} unique values, '{most_common}' is most common")
            
            insights.append(f"• Question: {question}")
            insights.append("• [Simulated AI Analysis - Set OPENAI_API_KEY for real AI insights]")
        
        return "\n".join(insights)
    
    def analyze_database_query(self, connection_name, query):
        """Combine database query with AI analysis"""
        
        # Execute query using database analytics
        df = self.db_analytics.execute_universal_query(connection_name, query)
        
        if df is not None and len(df) > 0:
            # Analyze results with AI
            insights = self.analyze_dataframe_with_ai(df, "What do these database results reveal?")
            
            return {
                'status': 'success',
                'query': query,
                'data': df.to_dict('records'),
                'ai_insights': insights,
                'summary': {
                    'rows': len(df),
                    'columns': list(df.columns)
                }
            }
        else:
            return {
                'status': 'error',
                'message': 'No data returned from query'
            }
