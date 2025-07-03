# Week 1: AI Agent Fundamentals

## Learning Goals
- Understand AI agent architecture patterns
- Set up and learn Flowise basics
- Build first customer service agent
- Document learning process
- Concurrently continue Codecademy Learning Python 2 for programming foundation

## Daily Progress

### Day 4: 07/03/2025
**Topics Studied:**
- Completed Codecademy Learn Python 2 course
- Explore pre-built templates in Flowise

### Day 3: 07/01/2025
**Topics Studied:**
- Flowise API Chatflow - Built weather chatbot with API request to https://openweathermap.org/
- Workflow: [ChatOpenAI with System Prompt] → [Conversation Agent] → [Custom Tool API call] → [Response] ← [Memory Buffer] 
  
**Key Insights:**
- API was more challenging, needed claude.ai to assist with Javascript for the custom tool.

**Challenges:**
- When I tried to save the first flow, I hit the maximum number of chatflows allowed in Flowise instance so I had to remove my Key test flow to make room.
- Missed setting up the parameter in the custom tool on the first round so no answers in the responses
- Once the tool was being called, it was returning "I have requested the current weather information for Austin" without actual data.  I was making the API call too complex based on what I had read at openweathermap.org. Simplifying the API call cleared up this issue.

### Day 2: 06/30/2025
**Topics Studied:**
- Flowise Chatflow - Built My first chatbot! Then updated it to handle questions based on a FAQ txt file.
- Workflow: [FAQ Document] → [Text Splitter] → [Vector Store] → [User Input] → [Retrieval QA Chain] ← [ChatOpenAI with System Prompt] → [Response] ← [Memory Buffer]
- Ran some questions by the basic txt data.  Then added a PDF file text splitter, replaced the txt connection with this and tested.  Success!

**Key Insights:**
- Switching between txt and pdf was very intuitive.  I am interested to find out how to link multiple data sources to my next version chatbot.

**Challenges:**
- I was trying to update the personality of the chatbot but I coulsn't find the system message on the ChatOpen API node.  Then I found that the system message is associated with the conversation chain node, which makes sense now.

### Day 1: 06/29/2025
**Topics Studied:**
- Get started in GitHub
- Get started on Flowise
- OpenAI API Key setup 

**Key Insights:**
- GitHub file structure is different than a regular folder system
- Flowise API Key test taught me a bit about how the chat flows work via troubleshooting.

**Challenges:**
- My github folder for week one is not organized as I would like but learning!
- Had trouble getting my OpenAPI Key validated but added notes on the api key test and what I learned

**Tomorrow's Plan:**
- Work in Flowise some more
- Spend more time on Python 2 training course that is in progress

---
## Week 1 Project: Customer Service Agent

### Project Description
Building a basic customer service agent that can handle frequently asked questions.

### Implementation
- **Flowise Version**: [cloud](https://cloud.flowiseai.com/)
- **Python Version**: N/A
### Files
- `flowise-workflow.json` - Exported Flowise configuration
- `screenshots/` - Agent workflow images
- `testing-notes.md` - How I tested the agent

## Resources Used This Week
- https://docs.github.com/en/get-started/start-your-journey/git-and-github-learning-resources

## Week 1 Project: Weather API chat bot

### Project Description
Building a basic customer service agent that can handle frequently asked questions.

### Implementation
- **Flowise Version**: [cloud](https://cloud.flowiseai.com/)
- **Python Version**: N/A
### Files
- `eek-01-foundations/Flowise/Weather API Chatbot/Weather Chatbot Chatflow.json` - Exported Flowise configuration
- `week-01-foundations/Flowise/Weather API Chatbot/Workflow Weather Screenshot 2025-07-01.png` - Agent workflow images
- `week-01-foundations/Flowise/Weather API Chatbot/troubleshooting.md` - Troubleshooting notes

## Resources Used This Week
- https://docs.github.com/en/get-started/start-your-journey/git-and-github-learning-resources
- https://openweathermap.org/api
- https://claude.ai/chat/troubleshootingAPI

## Reflection
[I'll add my thoughts on the week's learning at the end]
