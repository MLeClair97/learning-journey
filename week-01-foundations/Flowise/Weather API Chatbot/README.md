# Weather API Chatbot - Week 1 Project

## Project Overview
Built a weather chatbot using Flowise, connecting via an API to openweathermap.org 

## Implementation Details

### Components Used
- ChatOpenAI (gpt-3.5-turbo)
- Buffer Memory for conversation history
- Conversational Agent Node
- Custom Tool Node 

### Custom Tool
- Tool Name: get_current_weather
- Input schema: City, string, required
- Untilized Java script (ChatGPT assisted) linking to openweathermap.org per site API instructions
- API Key from openweathermap.org

## Testing Results
- Successfully connected to openweathermap.org using URL test: ✅
- Connected to openweathermap.org via API node: ✅
- Received weather for input (Austin): ✅
- Received lat and lon for Austin when requested to check other data: ✅

## Screenshots
- `week-01-foundations/Flowise/Weather API Chatbot/Workflow Weather Screenshot 2025-07-01.png` - Flowise canvas view & Sample conversation

## Lessons Learned
- Parameter Configuration: Must define all input parameters in Flowise tools - I missed this step initially
- It appeared on openweathermap.org that the request would require a lat and lon for a city so I added extra steps for geocoding API that were unneccessary.

## Files
- `week-01-foundations/Flowise/Weather API Chatbot/Weather Chatbot Chatflow.json` - Exportable workflow
