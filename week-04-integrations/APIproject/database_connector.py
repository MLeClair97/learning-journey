import sqlite3
import pandas as pd
import os

class UniversalDatabaseAnalytics:
    """Database connection and query execution"""
    
    def __init__(self):
        self.connections = {}
        self.setup_demo_database()
    
    def setup_demo_database(self):
        """Create demo database with sample data"""
        db_path = 'demo_business.db'
        
        # Create sample data if database doesn't exist
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
            print("✅ Demo database created with sample data")
        
        # Add the demo connection
        self.add_sqlite_connection('demo', db_path)
    
    def add_sqlite_connection(self, name, db_path):
        """Add SQLite connection"""
        self.connections[name] = {
            'type': 'sqlite',
            'path': db_path
        }
        print(f"✅ Added SQLite connection '{name}': {db_path}")
    
    def execute_universal_query(self, connection_name, query):
        """Execute query on specified database"""
        if connection_name not in self.connections:
            print(f"❌ Connection '{connection_name}' not found")
            return None
        
        try:
            conn_info = self.connections[connection_name]
            if conn_info['type'] == 'sqlite':
                conn = sqlite3.connect(conn_info['path'])
                df = pd.read_sql_query(query, conn)
                conn.close()
                print(f"✅ Query executed successfully on '{connection_name}'")
                return df
            else:
                print(f"❌ Connection type '{conn_info['type']}' not implemented yet")
                return None
        
        except Exception as e:
            print(f"❌ Query execution failed: {e}")
            return None

class MultiDatabaseQueryBuilder:
    """Advanced query building"""
    
    def __init__(self):
        self.query_history = []
    
    def build_query(self, table_name, columns=None, conditions=None, group_by=None):
        """Build SQL query dynamically"""
        
        # Select columns
        if columns:
            columns_str = ', '.join(columns)
        else:
            columns_str = '*'
        
        query = f"SELECT {columns_str} FROM {table_name}"
        
        # Add conditions
        if conditions:
            conditions_list = []
            for key, value in conditions.items():
                if isinstance(value, str):
                    conditions_list.append(f"{key} = '{value}'")
                else:
                    conditions_list.append(f"{key} = {value}")
            
            if conditions_list:
                query += " WHERE " + " AND ".join(conditions_list)
        
        # Add GROUP BY
        if group_by:
            if isinstance(group_by, list):
                query += f" GROUP BY {', '.join(group_by)}"
            else:
                query += f" GROUP BY {group_by}"
        
        # Store in history
        self.query_history.append(query)
        print(f"✅ Built query: {query}")
        
        return query