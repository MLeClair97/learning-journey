# fixed_all_in_one_api.py - Complete API with JSON serialization fix

from flask import Flask, request, jsonify
import pandas as pd
import sqlite3
import os
import json
import numpy as np
from datetime import datetime

# ============================================================================
# JSON SERIALIZATION FIX
# ============================================================================

class NumpyEncoder(json.JSONEncoder):
    """Custom JSON encoder for numpy data types"""
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        if isinstance(obj, pd.Timestamp):
            return obj.isoformat()
        if pd.isna(obj):
            return None
        return super(NumpyEncoder, self).default(obj)

def safe_json_response(data):
    """Create JSON response that handles numpy types"""
    try:
        # Convert data to JSON-safe format
        json_str = json.dumps(data, cls=NumpyEncoder, default=str)
        return json.loads(json_str)
    except Exception as e:
        print(f"JSON serialization error: {e}")
        return {"error": f"Data serialization failed: {str(e)}"}

# ============================================================================
# DATABASE SETUP
# ============================================================================

def setup_demo_database():
    """Create demo database with sample data"""
    db_path = 'demo_business.db'
    
    if not os.path.exists(db_path):
        conn = sqlite3.connect(db_path)
        
        # Create sample sales data
        sales_data = pd.DataFrame({
            'region': ['North', 'South', 'East', 'West', 'North', 'South'],
            'sales_amount': [50000, 75000, 60000, 40000, 55000, 80000],
            'orders': [120, 180, 140, 95, 130, 190],
            'month': ['Jan', 'Jan', 'Jan', 'Jan', 'Feb', 'Feb']
        })
        
        customers_data = pd.DataFrame({
            'customer_id': [1, 2, 3, 4, 5],
            'region': ['North', 'South', 'East', 'West', 'North'],
            'customer_type': ['Premium', 'Standard', 'Premium', 'Standard', 'Premium'],
            'total_value': [25000, 15000, 30000, 12000, 28000]
        })
        
        sales_data.to_sql('sales', conn, if_exists='replace', index=False)
        customers_data.to_sql('customers', conn, if_exists='replace', index=False)
        conn.close()
        
        print("✅ Demo database created")
    else:
        print("✅ Demo database exists")
    
    return db_path

# ============================================================================
# AI ANALYSIS (SIMULATED)
# ============================================================================

def simulate_ai_analysis(df, question):
    """Simulate AI analysis without requiring OpenAI API"""
    
    insights = []
    insights.append(f"📊 Dataset Analysis: {len(df)} records, {len(df.columns)} columns")
    
    # Analyze numeric columns
    numeric_cols = df.select_dtypes(include=['number']).columns
    if len(numeric_cols) > 0:
        for col in numeric_cols[:2]:
            avg_val = float(df[col].mean())  # Convert to Python float
            max_val = float(df[col].max())   # Convert to Python float
            min_val = float(df[col].min())   # Convert to Python float
            insights.append(f"💰 {col}: Range ${min_val:,.0f} - ${max_val:,.0f}, Average ${avg_val:,.0f}")
    
    # Analyze categorical columns
    categorical_cols = df.select_dtypes(include=['object']).columns
    if len(categorical_cols) > 0:
        col = categorical_cols[0]
        value_counts = df[col].value_counts()
        top_value = value_counts.index[0]
        top_count = int(value_counts.iloc[0])  # Convert to Python int
        insights.append(f"🏆 Top {col}: '{top_value}' ({top_count} occurrences)")
    
    insights.append(f"❓ Question: {question}")
    insights.append("🤖 [Simulated AI Analysis - Real OpenAI integration available]")
    
    return "\n".join(insights)

# ============================================================================
# DATABASE FUNCTIONS
# ============================================================================

def execute_query(query, db_path='demo_business.db'):
    """Execute SQL query and return DataFrame"""
    try:
        conn = sqlite3.connect(db_path)
        df = pd.read_sql_query(query, conn)
        conn.close()
        
        # Convert numpy types to Python types for JSON serialization
        for col in df.columns:
            if df[col].dtype == 'int64':
                df[col] = df[col].astype(int)
            elif df[col].dtype == 'float64':
                df[col] = df[col].astype(float)
        
        return df
    except Exception as e:
        print(f"❌ Query error: {e}")
        return None

def df_to_safe_dict(df):
    """Convert DataFrame to JSON-safe dictionary"""
    if df is None:
        return None
    
    # Convert to dict and ensure all values are JSON-serializable
    records = []
    for _, row in df.iterrows():
        record = {}
        for col, val in row.items():
            if pd.isna(val):
                record[col] = None
            elif isinstance(val, (np.integer, np.int64)):
                record[col] = int(val)
            elif isinstance(val, (np.floating, np.float64)):
                record[col] = float(val)
            else:
                record[col] = str(val)
        records.append(record)
    
    return records

# ============================================================================
# FLASK API
# ============================================================================

app = Flask(__name__)

# Setup database on startup
DB_PATH = setup_demo_database()

@app.route('/', methods=['GET'])
def home():
    """API documentation"""
    return jsonify(safe_json_response({
        'message': 'AI Analytics API is running! 🚀',
        'version': '1.0.0',
        'status': 'healthy',
        'endpoints': {
            'GET /': 'This documentation',
            'GET /api/health': 'Health check',
            'GET /api/demo/sales': 'Demo sales analysis',
            'GET /api/demo/customers': 'Demo customer analysis',
            'GET /api/test/simple': 'Simple test endpoint',
            'POST /api/analyze': 'Analyze custom data'
        },
        'quick_tests': [
            'curl http://localhost:5000/api/demo/sales',
            'curl http://localhost:5000/api/demo/customers',
            'curl http://localhost:5000/api/test/simple'
        ]
    }))

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check"""
    return jsonify(safe_json_response({
        'status': 'healthy',
        'service': 'AI Analytics API',
        'database': 'connected',
        'timestamp': datetime.now().isoformat()
    }))

@app.route('/api/test/simple', methods=['GET'])
def simple_test():
    """Simple test endpoint that should always work"""
    try:
        # Test basic functionality
        test_data = {
            'message': 'Simple test successful',
            'database_file_exists': os.path.exists('demo_business.db'),
            'python_version': 'working',
            'json_serialization': 'working'
        }
        
        return jsonify(safe_json_response(test_data))
        
    except Exception as e:
        return jsonify({'error': f'Simple test failed: {str(e)}'}), 500

@app.route('/api/demo/sales', methods=['GET'])
def demo_sales():
    """Demo: Sales analysis with proper JSON handling"""
    
    query = """
    SELECT 
        region,
        SUM(sales_amount) as total_sales,
        SUM(orders) as total_orders,
        AVG(sales_amount) as avg_sales
    FROM sales 
    GROUP BY region 
    ORDER BY total_sales DESC
    """
    
    try:
        df = execute_query(query)
        
        if df is not None and len(df) > 0:
            insights = simulate_ai_analysis(df, "What regional sales patterns should we focus on?")
            
            # Convert DataFrame to JSON-safe format
            safe_data = df_to_safe_dict(df)
            
            # Calculate summary with explicit type conversion
            total_sales = float(df['total_sales'].sum()) if len(df) > 0 else 0
            best_region = str(df.iloc[0]['region']) if len(df) > 0 else 'N/A'
            
            response_data = {
                'status': 'success',
                'query': query.strip(),
                'data': safe_data,
                'ai_insights': insights,
                'summary': {
                    'total_regions': len(df),
                    'best_region': best_region,
                    'total_sales': total_sales
                }
            }
            
            return jsonify(safe_json_response(response_data))
        else:
            return jsonify({'error': 'No data returned from query'}), 500
            
    except Exception as e:
        print(f"Sales demo error: {e}")
        return jsonify({'error': f'Sales analysis failed: {str(e)}'}), 500

@app.route('/api/demo/customers', methods=['GET'])
def demo_customers():
    """Demo: Customer analysis with proper JSON handling"""
    
    query = """
    SELECT 
        customer_type,
        COUNT(*) as customer_count,
        AVG(total_value) as avg_value,
        SUM(total_value) as total_value
    FROM customers 
    GROUP BY customer_type
    ORDER BY total_value DESC
    """
    
    try:
        df = execute_query(query)
        
        if df is not None and len(df) > 0:
            insights = simulate_ai_analysis(df, "How should we segment our customer base?")
            
            # Convert DataFrame to JSON-safe format
            safe_data = df_to_safe_dict(df)
            
            # Calculate summary with explicit type conversion
            total_customers = int(df['customer_count'].sum()) if len(df) > 0 else 0
            top_segment = str(df.iloc[0]['customer_type']) if len(df) > 0 else 'N/A'
            
            response_data = {
                'status': 'success',
                'query': query.strip(),
                'data': safe_data,
                'ai_insights': insights,
                'summary': {
                    'customer_segments': len(df),
                    'top_segment': top_segment,
                    'total_customers': total_customers
                }
            }
            
            return jsonify(safe_json_response(response_data))
        else:
            return jsonify({'error': 'No data returned from query'}), 500
            
    except Exception as e:
        print(f"Customer demo error: {e}")
        return jsonify({'error': f'Customer analysis failed: {str(e)}'}), 500

@app.route('/api/analyze', methods=['POST'])
def analyze_custom_data():
    """Analyze custom dataset"""
    try:
        data = request.get_json()
        
        if not data or 'dataset' not in data:
            return jsonify({'error': 'Missing dataset field'}), 400
        
        df = pd.DataFrame(data['dataset'])
        question = data.get('question', 'What insights can you provide?')
        
        if len(df) == 0:
            return jsonify({'error': 'Empty dataset'}), 400
        
        insights = simulate_ai_analysis(df, question)
        
        # Convert DataFrame info to JSON-safe format
        response_data = {
            'status': 'success',
            'insights': insights,
            'data_summary': {
                'rows': len(df),
                'columns': list(df.columns),
                'data_types': {col: str(dtype) for col, dtype in df.dtypes.items()}
            }
        }
        
        return jsonify(safe_json_response(response_data))
        
    except Exception as e:
        print(f"Custom analysis error: {e}")
        return jsonify({'error': f'Analysis failed: {str(e)}'}), 500

# ============================================================================
# ERROR HANDLERS
# ============================================================================

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'error': 'Endpoint not found',
        'available_endpoints': [
            '/',
            '/api/health',
            '/api/demo/sales',
            '/api/demo/customers',
            '/api/test/simple'
        ]
    }), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        'error': 'Internal server error',
        'message': 'Something went wrong on the server'
    }), 500

# ============================================================================
# STARTUP
# ============================================================================

if __name__ == '__main__':
    print("\n🚀 Starting AI Analytics API (Fixed Version)")
    print("📊 Database ready with demo data")
    print("🔗 API URL: http://localhost:5000")
    print("📖 Documentation: http://localhost:5000")
    print("\n💡 Quick tests:")
    print("   curl http://localhost:5000/api/test/simple")
    print("   curl http://localhost:5000/api/demo/sales")
    print("   curl http://localhost:5000/api/demo/customers")
    print("\n⏹️ Press Ctrl+C to stop\n")
    
    try:
        app.run(debug=False, port=5000, host='127.0.0.1')
    except OSError as e:
        if "Address already in use" in str(e):
            print("⚠️ Port 5000 busy, trying 5001...")
            app.run(debug=False, port=5001, host='127.0.0.1')
        else:
            print(f"❌ Startup error: {e}")
    except KeyboardInterrupt:
        print("\n👋 API stopped")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")