# Customer Service Agent - Week 1 Project

## Project Overview
Built a customer service agent using Flowise that can handle FAQs and maintain conversation context.

## Implementation Details

### Components Used
- ChatOpenAI (gpt-3.5-turbo)
- Buffer Memory for conversation history
- Retrieval QA Chain for FAQ lookup
- Text File loader / PDF file loader for knowledge base 

### Knowledge Base
- 5 FAQ entries covering common customer service topics in original text file
- Stored in `company-faq.txt`
- Product Quick Start Guide PDF for second round knowledge base
- Added customer service contact information to the Conversational Rectrieval QA Chain for questions not found in document.

### System Prompt
[Include your system prompt here]

## Testing Results
- Successfully handled greetings: ✅
- Answered FAQ questions accurately: ✅
- Maintained conversation context: ✅
- Escalated unknown issues appropriately: ✅

## Screenshots
- `week-01-foundations/customer-service-agent/Workflow Screenshot 2025-06-30.png` - Flowise canvas view
- `week-01-foundations/customer-service-agent/Chat Sample Screenshot 2025-06-30.png` - Sample conversation

## Lessons Learned
- I was trying to update the personality of the chatbot but I coulsn't find the system message on the ChatOpen API node. Then I found that the system message is associated with the conversation chain node, which makes sense now.
- The setup process seems logical and easy to establish once you understand the terminology for the pieces required.
- Learning the terminology for each node will take some time, but that will come with practice.

## Files
- `week-01-foundations/customer-service-agent/My FAQ Chatbot Chatflow.json` - Exportable workflow
- `week-01-foundations/customer-service-agent/company-faq.txt` - Knowledge base
- `week-01-foundations/customer-service-agent/SatFinder_Pro_Satellite_Meter_Quick_Start_Guide.pdf` - PDF Quick Guide for knowledge base
