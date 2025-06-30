# Week 1: AI Agent Fundamentals

## Learning Goals
- Understand AI agent architecture patterns
- Set up and learn Flowise basics
- Build first customer service agent
- Document learning process

## Daily Progress

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

### Day 2: 06/30/2025
**Topics Studied:**
- Flowise Chatflow - Built My first chatbot! Then updated it to handle questions based on a FAQ txt file.
- Workflow: [FAQ Document] → [Text Splitter] → [Vector Store] → [User Input] → [Retrieval QA Chain] ← [ChatOpenAI with System Prompt] → [Response] ← [Memory Buffer]
- Ran some questions by the basic txt data.  Then added a PDF file text splitter, replaced the txt connection with this and tested.  Success!

**Time Spent:**
- 

**Key Insights:**
- Switching between txt and pdf was very intuitive.  I am interested to find out how to link multiple data sources to my next version chatbot.

**Challenges:**
- I was trying to update the personality of the chatbot but I coulsn't find the system message on the ChatOpen API node.  Then I found that the system message is associated with the conversation chain node, which makes sense now.

**Tomorrow's Plan:**
- 
<!-- I'll add more days as I progress -->

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
- 

## Reflection
[I'll add my thoughts on the week's learning at the end]
