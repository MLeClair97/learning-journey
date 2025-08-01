import requests
import json

def test_api():
    """Test your API endpoints"""
    
    base_url = "http://localhost:5000"
    
    print("🧪 Testing AI Analytics API...\n")
    
    # Test 1: Health check
    print("1️⃣ Testing health check...")
    try:
        response = requests.get(f"{base_url}/api/health")
        if response.status_code == 200:
            print("✅ Health check passed")
            print(f"   Response: {response.json()}")
        else:
            print(f"❌ Health check failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Health check error: {e}")
    
    print("\n" + "="*50 + "\n")
    
    # Test 2: Demo sales analysis
    print("2️⃣ Testing demo sales analysis...")
    try:
        response = requests.get(f"{base_url}/api/demo/sales")
        if response.status_code == 200:
            result = response.json()
            print("✅ Sales analysis completed")
            print(f"   Query: {result.get('query', 'N/A')}")
            print(f"   Data rows: {result.get('summary', {}).get('rows', 'N/A')}")
            print(f"   AI Insights: {result.get('ai_insights', 'N/A')[:100]}...")
        else:
            print(f"❌ Sales analysis failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Sales analysis error: {e}")
    
    print("\n" + "="*50 + "\n")
    
    # Test 3: Custom data analysis
    print("3️⃣ Testing custom data analysis...")
    try:
        test_data = {
            "dataset": [
                {"product": "Widget A", "sales": 1000, "region": "North"},
                {"product": "Widget B", "sales": 1500, "region": "South"},
                {"product": "Widget C", "sales": 800, "region": "North"}
            ],
            "question": "Which products and regions are performing best?"
        }
        
        response = requests.post(f"{base_url}/api/analyze", json=test_data)
        if response.status_code == 200:
            result = response.json()
            print("✅ Custom analysis completed")
            print(f"   Insights: {result.get('insights', 'N/A')[:150]}...")
        else:
            print(f"❌ Custom analysis failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Custom analysis error: {e}")
    
    print("\n" + "="*50 + "\n")
    
    # Test 4: Query builder
    print("4️⃣ Testing query builder...")
    try:
        query_data = {
            "table": "customers",
            "columns": ["customer_type", "COUNT(*) as count"],
            "conditions": None,
            "connection": "demo"
        }
        
        response = requests.post(f"{base_url}/api/database/build-query", json=query_data)
        if response.status_code == 200:
            result = response.json()
            print("✅ Query builder completed")
            print(f"   Built query: {result.get('query', 'N/A')}")
            print(f"   Results: {len(result.get('data', []))} rows")
        else:
            print(f"❌ Query builder failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Query builder error: {e}")
    
    print("\n🎉 API testing complete!")

if __name__ == "__main__":
    print("⏰ Starting API tests in 3 seconds...")
    print("   Make sure your API is running first: python api.py")
    import time
    time.sleep(3)
    test_api()