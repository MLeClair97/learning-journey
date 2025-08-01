from flask import Flask, request, jsonify
import pandas as pd
from ai_analyst import AIDataAnalyst
from database_connector import MultiDatabaseQueryBuilder

app = Flask(__name__)

# Initialize your classes
ai_analyst = AIDataAnalyst()
query_builder = MultiDatabaseQueryBuilder()

@app.route('/', methods=['GET'])
def home():
    """API home page"""
    return jsonify({
        'message': 'AI Analytics API is running!',
        'available_endpoints': {
            'GET /': 'This help page',
            'GET /api/health': 'Health check',
            'POST /api/analyze': 'Analyze uploaded data',
            'POST /api/database/analyze': 'Analyze database query',
            'POST /api/database/build-query': 'Build and analyze query',
            'GET /api/demo/sales': 'Demo: Get sales analysis',
            'GET /api/demo/customers': 'Demo: Get customer analysis'
        }
    })

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'AI Analytics API',
        'database_connections': list(ai_analyst.db_analytics.connections.keys())
    })

@app.route('/api/analyze', methods=['POST'])
def analyze_data():
    """Analyze uploaded dataset"""
    try:
        data = request.get_json()
        
        if 'dataset' not in data:
            return jsonify({'error': 'Missing dataset field'}), 400
        
        df = pd.DataFrame(data['dataset'])
        question = data.get('question', 'What insights can you provide?')
        
        insights = ai_analyst.analyze_dataframe_with_ai(df, question)
        
        return jsonify({
            'status': 'success',
            'insights': insights,
            'data_summary': {
                'rows': len(df),
                'columns': list(df.columns)
            }
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/database/analyze', methods=['POST'])
def analyze_database():
    """Analyze database query with AI"""
    try:
        data = request.get_json()
        
        connection = data.get('connection', 'demo')
        query = data.get('query')
        
        if not query:
            return jsonify({'error': 'Missing query field'}), 400
        
        result = ai_analyst.analyze_database_query(connection, query)
        return jsonify(result)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/database/build-query', methods=['POST'])
def build_and_analyze_query():
    """Build query dynamically and analyze results"""
    try:
        data = request.get_json()
        
        table = data.get('table')
        columns = data.get('columns')
        conditions = data.get('conditions')
        
        if not table:
            return jsonify({'error': 'Missing table field'}), 400
        
        # Build query
        query = query_builder.build_query(table, columns, conditions)
        
        # Execute and analyze
        connection = data.get('connection', 'demo')
        result = ai_analyst.analyze_database_query(connection, query)
        
        return jsonify(result)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Demo endpoints for easy testing
@app.route('/api/demo/sales', methods=['GET'])
def demo_sales_analysis():
    """Demo: Analyze sales data"""
    query = "SELECT region, SUM(sales_amount) as total_sales, SUM(orders) as total_orders FROM sales GROUP BY region ORDER BY total_sales DESC"
    result = ai_analyst.analyze_database_query('demo', query)
    return jsonify(result)

@app.route('/api/demo/customers', methods=['GET'])
def demo_customer_analysis():
    """Demo: Analyze customer data"""
    query = "SELECT customer_type, COUNT(*) as count, AVG(total_value) as avg_value FROM customers GROUP BY customer_type"
    result = ai_analyst.analyze_database_query('demo', query)
    return jsonify(result)


# ============================================================================
# GET VERSIONS OF POST ENDPOINTS (for easy browser testing)
# ============================================================================

@app.route('/api/test/simple-query', methods=['GET'])
def test_simple_query():
    """GET version: Test a simple database query"""
    
    query = "SELECT region, sales_amount, orders FROM sales LIMIT 5"
    
    df = execute_query(query)
    
    if df is not None:
        insights = simulate_ai_analysis(df, "What do you see in this sample data?")
        
        return jsonify({
            'status': 'success',
            'test_type': 'Simple Database Query',
            'query': query,
            'data': df.to_dict('records'),
            'ai_insights': insights,
            'note': 'This is the GET version for easy browser testing'
        })
    else:
        return jsonify({'error': 'Query execution failed'}), 500

@app.route('/api/test/custom-analysis', methods=['GET'])
def test_custom_analysis():
    """GET version: Test custom data analysis"""
    
    # Sample data for testing
    sample_data = [
        {"product": "Widget A", "sales": 1000, "region": "North"},
        {"product": "Widget B", "sales": 1500, "region": "South"},
        {"product": "Widget C", "sales": 800, "region": "North"},
        {"product": "Widget D", "sales": 1200, "region": "East"}
    ]
    
    df = pd.DataFrame(sample_data)
    question = "Which products and regions are performing best?"
    
    insights = simulate_ai_analysis(df, question)
    
    return jsonify({
        'status': 'success',
        'test_type': 'Custom Data Analysis',
        'question': question,
        'sample_data': sample_data,
        'ai_insights': insights,
        'data_summary': {
            'rows': len(df),
            'columns': list(df.columns)
        },
        'note': 'This is the GET version for easy browser testing'
    })

@app.route('/api/test/all-endpoints', methods=['GET'])
def test_all_endpoints():
    """Test all functionality at once"""
    
    results = {}
    
    # Test 1: Database query
    try:
        sales_query = "SELECT region, SUM(sales_amount) as total FROM sales GROUP BY region"
        sales_df = execute_query(sales_query)
        if sales_df is not None:
            results['database_test'] = {
                'status': 'success',
                'rows': len(sales_df),
                'data': sales_df.to_dict('records')
            }
        else:
            results['database_test'] = {'status': 'failed', 'error': 'Query failed'}
    except Exception as e:
        results['database_test'] = {'status': 'failed', 'error': str(e)}
    
    # Test 2: AI analysis
    try:
        test_df = pd.DataFrame({
            'category': ['A', 'B', 'C'],
            'value': [100, 200, 150]
        })
        ai_result = simulate_ai_analysis(test_df, "Test analysis")
        results['ai_test'] = {
            'status': 'success',
            'insights': ai_result
        }
    except Exception as e:
        results['ai_test'] = {'status': 'failed', 'error': str(e)}
    
    # Test 3: Data processing
    try:
        sample_data = [{"x": 1, "y": 2}, {"x": 3, "y": 4}]
        test_df = pd.DataFrame(sample_data)
        results['data_processing_test'] = {
            'status': 'success',
            'processed_shape': test_df.shape,
            'processed_data': test_df.to_dict('records')
        }
    except Exception as e:
        results['data_processing_test'] = {'status': 'failed', 'error': str(e)}
    
    return jsonify({
        'overall_status': 'API is working!',
        'test_results': results,
        'timestamp': pd.Timestamp.now().isoformat()
    })

# ============================================================================
# DEBUGGING ENDPOINTS
# ============================================================================

@app.route('/api/debug/database', methods=['GET'])
def debug_database():
    """Debug database connection and tables"""
    
    try:
        # Check if database file exists
        db_exists = os.path.exists('demo_business.db')
        
        # Get table information
        tables_query = "SELECT name FROM sqlite_master WHERE type='table'"
        tables_df = execute_query(tables_query)
        
        # Get sample data from each table
        table_info = {}
        if tables_df is not None:
            for table in tables_df['name']:
                try:
                    sample_query = f"SELECT * FROM {table} LIMIT 3"
                    sample_df = execute_query(sample_query)
                    if sample_df is not None:
                        table_info[table] = {
                            'rows': len(execute_query(f"SELECT * FROM {table}")),
                            'columns': list(sample_df.columns),
                            'sample_data': sample_df.to_dict('records')
                        }
                except Exception as e:
                    table_info[table] = {'error': str(e)}
        
        return jsonify({
            'database_file_exists': db_exists,
            'database_path': 'demo_business.db',
            'tables_found': list(table_info.keys()) if table_info else [],
            'table_details': table_info
        })
        
    except Exception as e:
        return jsonify({'error': f'Database debug failed: {str(e)}'}), 500

@app.route('/api/debug/environment', methods=['GET'])
def debug_environment():
    """Debug Python environment and dependencies"""
    
    import sys
    
    try:
        # Check installed packages
        installed_packages = {}
        
        try:
            import flask
            installed_packages['flask'] = flask.__version__
        except ImportError:
            installed_packages['flask'] = 'NOT INSTALLED'
        
        try:
            import pandas
            installed_packages['pandas'] = pandas.__version__
        except ImportError:
            installed_packages['pandas'] = 'NOT INSTALLED'
        
        try:
            import sqlite3
            installed_packages['sqlite3'] = 'Built-in'
        except ImportError:
            installed_packages['sqlite3'] = 'NOT AVAILABLE'
        
        return jsonify({
            'python_version': sys.version,
            'installed_packages': installed_packages,
            'current_directory': os.getcwd(),
            'files_in_directory': os.listdir('.'),
            'environment_status': 'All systems operational'
        })
        
    except Exception as e:
        return jsonify({'error': f'Environment debug failed: {str(e)}'}), 500

# ============================================================================
# UPDATED HOME PAGE WITH ALL TEST LINKS
# ============================================================================

@app.route('/', methods=['GET'])
def home():
    """Updated API documentation with test links"""
    return jsonify({
        'message': 'AI Analytics API is running! 🚀',
        'version': '1.0.0',
        'status': 'healthy',
        
        'browser_friendly_endpoints': {
            'GET /': 'This documentation',
            'GET /api/health': 'Health check',
            'GET /api/demo/sales': 'Demo sales analysis',
            'GET /api/demo/customers': 'Demo customer analysis',
            'GET /api/test/simple-query': 'Test database query',
            'GET /api/test/custom-analysis': 'Test custom data analysis',
            'GET /api/test/all-endpoints': 'Test all functionality',
            'GET /api/debug/database': 'Debug database connection',
            'GET /api/debug/environment': 'Debug Python environment'
        },
        
        'post_endpoints_need_curl': {
            'POST /api/analyze': 'Analyze custom data (use curl)',
            'POST /api/database/analyze': 'Analyze database query (use curl)'
        },
        
        'quick_browser_tests': [
            'http://localhost:5000/api/demo/sales',
            'http://localhost:5000/api/test/simple-query',
            'http://localhost:5000/api/test/all-endpoints',
            'http://localhost:5000/api/debug/database'
        ],
        
        'curl_examples': [
            'curl http://localhost:5000/api/demo/sales',
            'curl -X POST http://localhost:5000/api/analyze -H "Content-Type: application/json" -d \'{"dataset": [{"x": 1}], "question": "test"}\''
        ]
    })

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
            '/api/test/simple-query',
            '/api/test/all-endpoints'
        ]
    }), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        'error': 'Internal server error',
        'message': 'Something went wrong on the server',
        'debug_endpoint': '/api/debug/environment'
    }), 500

if __name__ == '__main__':
    print("\n🚀 Starting AI Analytics API...")
    print("📊 Demo database created with sample data")
    print("🔗 Available at: http://localhost:5000")
    print("📖 Visit http://localhost:5000 for API documentation")
    print("\n💡 Quick test: curl http://localhost:5000/api/demo/sales")
    print("\n⏹️  Press Ctrl+C to stop the server\n")
    
    app.run(debug=True, port=5000)