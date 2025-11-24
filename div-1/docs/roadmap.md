# Roadmap for Jarvis-like Assistant (Nov 24 – Dec 31, 2025)

## Week 1 (Nov 24 – Dec 1, 2025)

*   **Tech Stack & Environment Setup**: Decide on a local-first architecture. For example, one project used FastAPI for the Python backend and Ollama to host open-source LLMs locally ([medium.com](medium.com), [medium.com](medium.com)).
    *   Install Python (3.11+), set up a virtualenv, and install FastAPI/Uvicorn plus key libraries (LangChain or LlamaIndex).
    *   Choose and install a local LLM: e.g. install Ollama and pull a model (`ollama pull llama3`) or prepare llama.cpp.
    *   Ensure tooling for GPU (CUDA) is in place if needed. Plan for using free alternatives (OpenAI/Gemini) only for prototyping if local models aren’t ready ([learndatasci.com](learndatasci.com), [huggingface.co](huggingface.co)).

*   **Local LLM Prototype**: Run a small model locally to verify setup. For example, execute `ollama run llama3` and interact via the Python client or CLI ([learndatasci.com](learndatasci.com)).
    *   Alternatively, install and run llama.cpp: compile it and run `llama-cli -hf <model.GGUF>` or `llama-server` on a GGUF model ([huggingface.co](huggingface.co)).
    *   Test a basic prompt (e.g. “Hello, Jarvis”) to confirm the model responds. If local installation proves difficult, use a free API (OpenAI/Gemini) for now, but plan to switch ([datacamp.com](datacamp.com), [datacamp.com](datacamp.com)).

*   **FastAPI Skeleton**: Create a FastAPI app. In `main.py`, do something like `app = FastAPI()` and include a router for endpoints ([datacamp.com](datacamp.com)).
    *   Define a placeholder endpoint (e.g. `@app.post("/ask")`) that accepts JSON or query text.
    *   Test that `uvicorn main:app --reload` runs and visit `/docs` to see Swagger UI ([datacamp.com](datacamp.com)).
    *   For now, this endpoint can return a dummy message. Ensure logging is set up (e.g. Python’s logging module) to capture startup info.

## Week 2 (Dec 1 – Dec 8, 2025)

*   **Data Ingestion Pipeline**: Implement ingestion for one personal data source. For example, export a WhatsApp chat text file and write a parser that reads each line and extracts timestamp, sender, and content ([medium.com](medium.com), [medium.com](medium.com)).
    *   Optionally, group messages into conversation chunks (e.g. start a new chunk if >30 min gap) ([medium.com](medium.com)).
    *   Store raw entries or chunks in a local file/DB for processing. Verify parsing by printing sample messages.

*   **Embedding & Vector Store Setup**: Convert ingested text to embeddings and index them.
    *   Load the parsed text chunks and create embeddings (using a model like SentenceTransformers or OpenAI embeddings).
    *   Use a vector database (Chroma, FAISS, or similar). For example, one tutorial loads documents, splits into chunks, and creates a FAISS store with `FAISS.from_documents(...)` ([datacamp.com](datacamp.com)).
    *   Integrate via LangChain or LlamaIndex: e.g. use LangChain’s TextSplitter and FAISS or LlamaIndex’s GPTVectorStoreIndex ([datacamp.com](datacamp.com), [developers.llamaindex.ai](developers.llamaindex.ai)).

*   **Memory Retrieval Test**: Build a retriever and test queries.
    *   From the vector store, create a retriever object (e.g. `vector_store.as_retriever()`). Run `retriever.get_relevant_documents("some query")` on a sample question to see if it returns expected chat chunks ([datacamp.com](datacamp.com)).
    *   Alternatively, use LlamaIndex’s Memory class which internally handles short-term and long-term memory ([developers.llamaindex.ai](developers.llamaindex.ai)).
    *   Confirm that querying the index with sample questions yields relevant past entries.

## Week 3 (Dec 8 – Dec 15, 2025)

*   **Integrate Retrieval + LLM**: In the FastAPI endpoint (e.g. `/ask`), wire up the RAG pipeline.
    *   Upon receiving user input, fetch relevant memory from the vector store (as above).
    *   Concatenate the returned chunks into a context string.
    *   Build a prompt like: “Use the following information to answer the question:\n\n{context}\n\nQuestion: {user_query}”.
    *   Then call the LLM with this prompt (via Ollama’s Python client or an API). For example, use `retriever.get_relevant_documents(query)` and then `llm.generate(prompt)` to produce an answer ([datacamp.com](datacamp.com)).
    *   Return the LLM’s response in the API JSON.

*   **API Endpoint & Error Handling**: Finalize the `/ask` endpoint code.
    *   Use FastAPI’s async support for non-blocking calls.
    *   Wrap calls in try/except to catch LLM or retrieval errors and return HTTP 500 if needed.
    *   Log each incoming request, the number of documents retrieved, and the LLM response time.
    *   Test end-to-end by querying `/ask?text=...` and ensure the response is coherent and uses past data. Use the Swagger UI or curl to validate parameters and outputs.

*   **Short-term Chat Memory (Optional)**: (Stretch goal) Keep track of the current conversation turn.
    *   You may append the user’s last message and the assistant’s reply to an in-memory chat history buffer (FIFO).
    *   This can then be included as additional context on subsequent calls. At minimum, ensure the vector-store retrieval is happening correctly each turn.

## Week 4 (Dec 15 – Dec 22, 2025)

*   **Code Refactoring**: Refactor the project for modularity.
    *   Separate code into modules like `ingest.py` (data parsing and indexing), `memory.py` (vector store interface), `models.py` (LLM interface), and `api.py` (FastAPI routes).
    *   Ensure functions have clear inputs/outputs. This aligns with good architecture (e.g. [25†L694-L701] splits routing logic).
    *   Aim for a clean API layer that calls into reusable functions.

*   **Automated Testing**: Write unit tests (`pytest`) for each core component:
    *   Verify the parser outputs correct fields.
    *   Verify the embedding/indexing works (e.g. known text returns expected vectors).
    *   Verify the retrieval returns expected items for a test query.
    *   Also test the FastAPI endpoints using Starlette’s test client. Check that invalid inputs (empty query, etc.) are handled gracefully.

*   **Add Another Ingestion Stream (Optional)**: If time, ingest a second data type (e.g. a CSV of contacts or a Google Takeout JSON).
    *   Abstract the ingestion code so you can plug in a new loader with minimal changes. For example, implement a generic `load_documents(source)` function.
    *   Ensure your vector store can combine multiple sources.

*   **Logging & Monitoring**: Enhance logging (timestamps, log levels).
    *   For example, log every query and response pair, and any errors.
    *   Consider writing logs to a file or stdout in structured (JSON) format. This sets up scalability and debuggability.

## Week 5 (Dec 22 – Dec 29, 2025)

*   **End-to-End Validation**: Simulate realistic use.
    *   Create scenarios (e.g. “When did I last talk about the project?”) and verify the system answers correctly using the ingested data.
    *   Test edge cases (no relevant memory, large query, etc.).
    *   Confirm that the assistant does not leak irrelevant data.

*   **Performance Check**: Measure response time for typical queries.
    *   If it’s too slow, consider optimizations: smaller model, increase retrieval k to fetch more docs if missing info, or cache recent queries.
    *   Since 10–15 hrs/week is limited, focus on correctness over heavy optimization.
    *   Ensure the system can handle at least a few concurrent requests (FastAPI’s async helps here).

*   **Documentation**: Prepare concise docs/README.
    *   Describe how to set up and run the backend, how to add new data, and how to call the API.
    *   Document the endpoints (`/ask`, any other routes) with example inputs/outputs.
    *   If Swagger UI is enabled, note its URL. This completes the “clean API for future integration” goal.

*   **Demo Script**: Write a short script or notes showing example usage (e.g. sending a chat message to the API and printing the response). This serves as a proof-of-concept for future UI integration.

## Week 6 (Dec 29 – Dec 31, 2025)

*   **Final Review & Polish**: Do one last pass on all code.
    *   Remove debug prints, ensure environment variables (like API keys) are used instead of hardcoding.
    *   Run through the full flow one more time. Verify that logs are readable and no errors remain.

*   **Launch Prep**: “Deploy” the MVP on your machine or a server (even if it’s just `uvicorn main:app`).
    *   Ensure the backend can start up on its own.
    *   Tag the code as the initial release.
    *   Prepare any brief release notes summarizing capabilities and known limitations.

*   **Launch Day**: Declare the initial version launched.
    *   At minimum, share that the backend is running and tested on sample data.
    *   Optionally, share the API docs with any stakeholders or keep it for yourself as the foundation for future UI development.