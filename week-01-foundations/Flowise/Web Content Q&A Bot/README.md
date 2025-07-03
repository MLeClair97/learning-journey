# Web Content Q&A Bot - Project Notes
Updated 07/03/2025

## Project Overview
Built a web content Q&A chatbot using Flowise that can scrape websites and answer questions based on the scraped content. This project bridges FAQ chatbot skills with web data retrieval capabilities.

## Skills Developed
- Web content scraping and processing
- Vector database integration (in-memory)
- RAG (Retrieval-Augmented Generation) fundamentals
- Document chunking and embedding

## Technical Components

### Flow Architecture
```
Cheerio Web Scraper → Recursive Character Text Splitter → In-Memory Vector Store → Conversational Retrieval QA Chain
                                                            ↑
                                                     OpenAI Embeddings
```

### Node Configuration
1. **Cheerio Web Scraper**
   - URL: `https://masienda.com/pages/story`
   - Text Splitter: Connected to Recursive Character Text Splitter
   - Output: Document format

2. **Recursive Character Text Splitter**
   - Chunk Size: 1000 characters
   - Chunk Overlap: 200 characters
   - Input: Raw web content
   - Output: Chunked documents

3. **OpenAI Embeddings**
   - Model: `text-embedding-ada-002`
   - Connected to Vector Store for document embedding

4. **In-Memory Vector Store**
   - Document Input: From text splitter
   - Embeddings: From OpenAI Embeddings
   - Retriever: Memory Retriever (Top K: 4)

5. **Conversational Retrieval QA Chain**
   - Chat Model: GPT-3.5-turbo
   - Vector Store Retriever: Connected to vector store
   - Memory: Conversation Summary Buffer Memory
   - Custom prompts for context-aware responses

### Prompt Engineering

**Rephrase Prompt:**
```
Given the following conversation and a follow up question, rephrase the follow up question to be a standalone question.

Chat History:
{chat_history}

Follow Up Input: {question}

Standalone Question:
```

**Response Prompt:**
```
I want you to act as a document that I am having a conversation with. Your name is "AI Assistant". Using the provided context, answer the user's question to the best of your ability using the resources provided.

Context: {context}

If there is nothing in the context relevant to the question at hand, just say "I don't have information about that in the current context."

Question: {question}
Answer:
```

## Testing Results

### Successful Tests
✅ **Basic Web Scraping**: Successfully scraped Masienda website content
✅ **Question Answering**: Correctly answered "What is Masienda?" with detailed information from scraped content
✅ **Context Integration**: Bot properly used scraped content to provide relevant answers
✅ **Conversation Flow**: Maintained conversation history and context

### Issues Encountered
❌ **Williams Sonoma Blocking**: Original target site (williams-sonoma.com) appeared to block scraping
❌ **Complex Prompt Updates**: Adding multi-URL support caused response delays
❌ **Performance**: Some queries took longer than expected to process

## Lessons Learned

1. **Website Compatibility**: Not all websites allow scraping - test with scraper-friendly sites first
2. **Prompt Variables**: Critical to include correct variables (`{context}`, `{question}`, `{chat_history}`) in prompts
3. **Vector Store Necessity**: Conversational Retrieval QA Chain requires vector store, not raw text
4. **Incremental Testing**: Better to test each component before adding complexity

## Next Steps (Phase 2)

### Multi-URL Support Options
1. **URL Router Function**: JavaScript function to route URLs based on keywords
2. **Multiple Scrapers**: Separate scraper nodes for different websites
3. **User Choice**: Let users specify which website to scrape

### Potential Improvements
- Add error handling for failed web requests
- Implement caching for frequently accessed pages
- Add support for dynamic content (JavaScript-rendered pages)
- Create URL validation and sanitization
- Add rate limiting for web requests

### Vector Store Integration
- In-Memory Vector Store works well for testing but doesn't persist data
- Embeddings are crucial for search within scraped content but use a larger amount of tokens

### Web Scraping Considerations
- Static HTML content works best with Cheerio
- Some sites block automated scraping (use robots.txt compliant sites)
- Consider implementing retry logic for failed requests

## Files and Configuration
- **Flowise Flow**: Web Content Q&A Bot
- **Test URL**: https://masienda.com/pages/story
- **Model**: GPT-3.5-turbo with OpenAI embeddings
- **Vector Store**: In-Memory (for development)

## Resources Used
- Flowise visual flow builder
- OpenAI API (GPT-3.5-turbo, text-embedding-ada-002)
- Cheerio web scraping library
- In-memory vector storage

---

**Status**: ✅ Basic functionality working  
**Next Session**: Implement multi-URL support and error handling  
**Time Invested**: ~2 hours  
**Difficulty**: Intermediate
