# AI Chatbot Architecture: Vector Databases vs APIs

## Key Concepts

### Relational vs Vector Databases
- **Relational databases**: Store structured data in tables (rows/columns), find exact matches
- **Vector databases**: Store data as mathematical vectors representing meaning/characteristics, find similar items
- **Key difference**: Relational = "Find exact matches", Vector = "Find similar content"

### Embeddings (Vector Representations)
- Convert any data type (text, images, audio, structured data) into lists of numbers
- Capture essential "meaning" or characteristics of data
- Similar concepts have similar vector values (e.g., "cat" and "dog" vectors would be close)
- Enable semantic similarity searches rather than just keyword matching
- Created by machine learning models analyzing massive datasets

### How AI Chatbots Work
Basic flow for modern AI chatbots:
1. User asks question
2. Convert question to embedding vector
3. Search vector database for similar content
4. Retrieve relevant information
5. Generate response using retrieved context

This is called **RAG (Retrieval-Augmented Generation)**

## Architecture Patterns

### Static Data → Vector Stores + Embeddings
**Best for:**
- Product catalogs
- Company wikis  
- FAQ databases
- Documentation
- Policy manuals
- Knowledge bases
- Training materials

**Process:**
1. **Phase 1 (Setup)**: Scrape/Load → Chunk → Embed → Store
2. **Phase 2 (Runtime)**: Question → Embed → Search → Retrieve → Generate

### Dynamic Data → API Calls
**Best for:**
- Weather conditions
- Stock prices
- Sports scores
- News updates
- Account balances
- Real-time inventory
- Current user status

**Process:**
- Direct API call for current information
- Minimal token usage
- Real-time accuracy

### Hybrid Approach
Many systems combine both:
- Vector search for product descriptions (static)
- API calls for current pricing/inventory (dynamic)
- Vector search for FAQs (static)
- API calls for order status (dynamic)

## Token Usage Analysis

### High Token Usage (Vector/RAG Systems)
- **Embedding creation**: Every chunk of content → embeddings
- **Retrieval context**: Multiple relevant chunks sent to LLM
- **Longer prompts**: System prompt + retrieved context + user question + history

### Low Token Usage (API Systems)
- Concise, structured data from APIs
- No large context retrieval needed
- Simple prompt structure

### Token Types
- **Input tokens**: Question + system prompt + retrieved context
- **Output tokens**: Bot's response  
- **Embedding tokens**: Text → vectors (separate pricing, usually cheaper)

## Flowise Architecture Examples

### Web Content Q&A Bot Flow
```
Web Scraper → Text Splitter → OpenAI Embeddings → Vector Store
                                      ↓
User Question → Conversational Retrieval QA Chain → Response
```

### Weather Chatbot Flow
```
User Question → Conversational Agent → Custom Tool (API) → Response
```

### Key Processing Nodes
- **Conversational Retrieval QA Chain**: Main LLM processing (expensive tokens)
- **Conversational Agent**: LLM processing + tool decision making
- **Vector Store Retriever**: Mathematical search (no tokens)
- **OpenAI Embeddings**: Text → vectors (embedding tokens)

## Decision Framework

### When to Use Vector Stores
- Static or semi-static content
- Need semantic similarity
- Large knowledge bases
- Content that changes monthly/yearly

### When to Use APIs
- Real-time data requirements
- Precise, factual information
- Data that changes hourly/daily
- Structured responses

### Cost Considerations
- Vector stores: High setup cost, moderate ongoing costs
- APIs: Low setup cost, pay-per-use
- Token usage is the primary cost driver for LLM processing

## Key Takeaways
1. **Architecture choice depends on data freshness needs**
2. **Vector stores excel at semantic similarity, APIs at real-time accuracy**
3. **Token costs come from LLM processing, not retrieval operations**
4. **Hybrid approaches often provide the best user experience**
5. **The "QA Chain" or "Agent" nodes are where your token budget gets consumed**