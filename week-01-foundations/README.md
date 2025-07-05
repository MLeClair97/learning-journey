# Week 1: AI Agent Fundamentals

## Learning Goals
- Understand AI agent architecture patterns
- Set up and learn Flowise basics
- Build first customer service agent
- Document learning process
- Concurrently continue Codecademy Learning Python 2 for programming foundation

## Daily Progress

### Day 5: 07/05/2025
**Topics Studied**
- Reviewed Flowise chatbots built this week to understand the differences between their fuctionality
- Attempted my first Agentflow with a basic math function.  

**Key Insigths**
- I now understand, on a high level, embeddings and vector data vs API calls, where the work is being done in each of these, and how that affects the token use.
- I also understand promt engineering best practices.  I have done many promts and refined them as I went along, in an interative process.  The results are much more helpful after fine tuning the prompt.
- A full summary of what I learned is in noted in week-01-foundations/Flowise/ai_flowise_summary_notes_from_week1.md
- Lots to learn on the Flowies Agentflow side.  I did some loops trying to figure out how to get a tool set up after the agent in the flow - which led to lots of issues.  Then I realized that the agent could call the chatflows as a tool in the agent node, so I simplified my agent and just called a chatflow math tool that I built.
- Notes on Agents vs Chatflows:

### Day 4: 07/03/2025
**Topics Studied:**
- Completed Codecademy Learn Python 2 course
- Built a basic Web Content Q&A bot with a web scraper node on Flowise

**Key Insights**
- Embeddings for the Web Content Q&A chat bot take a lot more tokens than a simple chat bot.  I used 33.035M input tokens today vs 53K for all other chat projects.
  
**Challenges:**
- The first site I chose (williams-sonoma.com) did not work.  I changed the URL and had a successful response.
- When trying to move to more than one site for responses, the bot took a long time and did not answer.  I went back to one site and then got a message that I had maxed out my OpenAI request for today.  Stopping at one website Q&A for today, and will revisit the multi-site option another time.
  

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
