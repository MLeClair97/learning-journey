# # AI Analytics API
# 
# Complete REST API for AI-powered data analysis combining SQL and OpenAI.
# 
# ## Quick Start
# 
# 1. Install dependencies:
#    ```bash
#    pip install flask pandas requests openai python-dotenv
#    ```
# 
# 2. (Optional) Set OpenAI API key:
#    ```bash
#    export OPENAI_API_KEY="your-key-here"
#    ```
# 
# 3. Run the API:
#    ```bash
#    python api.py
#    ```
# 
# 4. Test the API:
#    ```bash
#    python test_api.py
#    ```
# 
# ## API Endpoints
# 
# - `GET /` - API documentation
# - `GET /api/health` - Health check
# - `GET /api/demo/sales` - Demo sales analysis
# - `POST /api/analyze` - Analyze custom data
# - `POST /api/database/analyze` - Analyze database query
# 
# ## Example Usage
# 
# ```bash
# curl http://localhost:5000/api/demo/sales
# ```
