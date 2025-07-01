# Flowise Weather Chatbot - Troubleshooting Guide

## Project Overview
Building a weather API chatbot using Flowise with OpenWeatherMap API integration.

## Initial Setup Issues

### Problem 1: Chatflow Limit Exceeded
**Error**: `Failed to retrieve Chatflow: Limit exceeded: flows`

**Root Cause**: Hit the maximum number of chatflows allowed in Flowise instance

**Solution**:
- Delete unused/test chatflows to free up slots

**Lesson Learned**: Always check instance limits before starting new projects

---

## Custom Tool Configuration Issues

### Problem 2: Tool Not Receiving Parameters
**Error**: `The weather in Austin is currently not available`

**Root Cause**: Custom tool wasn't properly configured to accept city parameter

**Initial Code Issues**:
```javascript
// ❌ This wasn't working - no parameter configuration
const getWeather = async (city) => {
    // Function expecting city but not receiving it
}
```

**Solution Steps**:
1. **Configure Tool Parameters**:
   - Parameter Name: `city`
   - Type: `string`
   - Description: `The name of the city to get weather for`
   - Required: `true`

2. **Updated Code Structure**:
```javascript
// ✅ Proper parameter handling
return await getWeather(city);
```

**Lesson Learned**: Always define input parameters explicitly in Flowise custom tools

---

### Problem 3: Tool Recognition But No Response
**Error**: Tool being called but returning "I have requested the current weather information for Austin" without actual data

**Root Cause**: Multiple potential issues in API implementation

**Debugging Process**:

#### Attempt 1: Geocoding API Approach
```javascript
// ❌ This was overly complex and introduced failure points
const url = `https://api.openweathermap.org/geo/1.0/direct?q=${city}&limit=5&appid=${API_KEY}`;
// Two-step process: geocoding → weather API
```

**Issues with this approach**:
- Multiple API calls increase failure points
- Async/await complexity in Flowise environment

#### Attempt 2: Direct Weather API (SUCCESSFUL)
```javascript
// ✅ This worked - simpler, more reliable
const url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${API_KEY}&units=metric`;
```

**Why this worked**:
- Single API call
- Simpler error handling
- Direct city name lookup
- Proven to work when tested in browser

**Lesson Learned**: Start with the simplest API approach first, then add complexity if needed

---

## API Integration Best Practices

### API Key Management
- ✅ Verify API key is active in OpenWeatherMap dashboard
- ✅ Test API endpoint in browser before implementing
- ✅ Use meaningful error messages for debugging

### Error Handling Strategy
```javascript
try {
    const response = await axios.get(url);
    const data = response.data;
    return `Weather in ${data.name}: ${data.weather[0].description}...`;
} catch (error) {
    if (error.response && error.response.status === 404) {
        return `Sorry, I couldn't find weather information for "${city}".`;
    }
    return `Sorry, there was an error getting weather data: ${error.message}`;
}
```

### Code Structure That Works
```javascript
const axios = require('axios');

const getWeather = async (city) => {
    const API_KEY = 'your_actual_api_key_here';
    const url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${API_KEY}&units=metric`;
    
    try {
        const response = await axios.get(url);
        const data = response.data;
        
        return `Weather in ${data.name}: ${data.weather[0].description}, Temperature: ${data.main.temp}°C, Feels like: ${data.main.feels_like}°C, Humidity: ${data.main.humidity}%`;
        
    } catch (error) {
        if (error.response && error.response.status === 404) {
            return `Sorry, I couldn't find weather information for "${city}". Please check the city name and try again.`;
        }
        return `Sorry, there was an error getting weather data: ${error.message}`;
    }
};

return await getWeather(city);
```

---

## Final Working Architecture

### Node Configuration:
1. **ChatOpenAI**: GPT-3.5-turbo model
2. **Conversation Summary Buffer Memory**: Token limit 1000
3. **Conversational Agent**: Connects LLM, memory, and tools
4. **Custom Tool**: Weather API integration with proper parameter configuration

### Successful Test Cases:
- ✅ "What is the weather in Austin?" → Returns formatted weather data
- ✅ "What is the lat and lon in Austin" → Returns formatted geo location data
- ✅ Invalid city names → Returns helpful error message

---

## Key Takeaways

1. **Start Simple**: Use direct API calls before complex multi-step processes
2. **Test Externally First**: Always verify API endpoints work in browser/Postman
3. **Parameter Configuration**: Explicitly define all input parameters in Flowise tools
4. **Error Handling**: Implement comprehensive error handling with meaningful messages
5. **Documentation**: Keep detailed notes of what worked and what didn't

---

## Resources
- [OpenWeatherMap API Documentation](https://openweathermap.org/api)
- [Flowise Documentation](https://docs.flowiseai.com/)
- [Working Project Repository](week-01-foundations/Flowise/Weather API Chatbot/README.md)

---

*Last Updated: 07/01/2025*
*Status: ✅ Working Solution*
