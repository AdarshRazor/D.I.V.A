# Project D.I.V.A - Master Task List

**Status Legend:**
*   🔴 **Pending**: Not started.
*   🟡 **In Progress**: Currently being worked on.
*   🟢 **Completed**: Finished and verified.

**Priority Legend:**
*   **P0**: Critical (Blocker)
*   **P1**: High (Core Feature)
*   **P2**: Medium (Enhancement)
*   **P3**: Low (Nice to have)

## Phase 1: The Skeleton & The Brain (Week 1)
| ID | Task Name | Description | Status | Priority | Dependency |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1.1** | Setup Environment | Initialize Git repo, create virtualenv, install Python 3.11+. | 🔴 | **P0** | - |
| **1.2** | Install Dependencies | Install FastAPI, Uvicorn, Loguru, Pydantic, python-dotenv. | 🔴 | **P0** | 1.1 |
| **1.3** | Setup Local LLM | Install Ollama and pull `llama3.2` model. Verify CLI response. | 🔴 | **P1** | 1.1 |
| **1.4** | FastAPI Skeleton | Create `main.py` with basic CORS, Middleware, and Health Check endpoint. | 🔴 | **P0** | 1.2 |
| **1.5** | Integrate Gemini API | Create `brain.py` service to handle calls to Google Gemini 1.5 Flash. | 🔴 | **P0** | 1.4 |
| **1.6** | Setup Logging | Configure Loguru to write structured logs to `logs/app.log`. | 🔴 | **P1** | 1.4 |
| **1.7** | Milestone Check 1 | Verify API responds to "Hello" via curl/Postman and logs the event. | 🔴 | **P0** | 1.5, 1.6 |

## Phase 2: The Hippocampus (Memory) (Week 2)
| ID | Task Name | Description | Status | Priority | Dependency |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **2.1** | Install ChromaDB | Install `chromadb` and `sentence-transformers`. | 🔴 | **P0** | 1.2 |
| **2.2** | Vector Store Setup | Create `memory.py` to initialize ChromaDB client and collection. | 🔴 | **P0** | 2.1 |
| **2.3** | Build `/ingest` API | Create endpoint to accept text/JSON, chunk it, and store embeddings. | 🔴 | **P0** | 2.2, 1.4 |
| **2.4** | Implement RAG Logic | Modify `/ask` endpoint to query ChromaDB for context before calling LLM. | 🔴 | **P0** | 2.3, 1.5 |
| **2.5** | Milestone Check 2 | Ingest a fact ("My color is Blue"), restart server, and verify recall. | 🔴 | **P0** | 2.4 |

## Phase 3: The Senses (Data Ingestion) (Week 3)
| ID | Task Name | Description | Status | Priority | Dependency |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **3.1** | WhatsApp Loader | Create `loader_whatsapp.py` to parse exported chat logs into chunks. | 🔴 | **P1** | 2.3 |
| **3.2** | File Loader | Create `loader_files.py` to scan directories for PDF/TXT/MD files. | 🔴 | **P1** | 2.3 |
| **3.3** | Ingestion Pipeline | Connect loaders to the `/ingest` endpoint for batch processing. | 🔴 | **P1** | 3.1, 3.2 |
| **3.4** | Milestone Check 3 | Feed a resume/chat log and ask specific questions about it. | 🔴 | **P1** | 3.3 |

## Phase 4: The "Kid" Personality (Week 4)
| ID | Task Name | Description | Status | Priority | Dependency |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **4.1** | User Profile Store | Implement `user_profile.json` for explicit fact storage (non-vector). | 🔴 | **P2** | 2.2 |
| **4.2** | System Prompting | Refine system prompt to define "Jarvis" persona and rules. | 🔴 | **P1** | 1.5 |
| **4.3** | Context Awareness | Inject time of day and user name into every prompt context. | 🔴 | **P2** | 4.2 |
| **4.4** | Milestone Check 4 | Verify distinct personality and context awareness in responses. | 🔴 | **P2** | 4.3 |

## Phase 5: Polish & Launch (Week 5)
| ID | Task Name | Description | Status | Priority | Dependency |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **5.1** | Basic UI | Build a simple Streamlit or HTML/JS frontend for easier chatting. | 🔴 | **P3** | 1.4 |
| **5.2** | Stress Testing | Send malformed data and high volume requests to test stability. | 🔴 | **P2** | 1.7 |
| **5.3** | Documentation | Write `README.md` with setup instructions and API usage. | 🔴 | **P2** | - |
| **5.4** | Final Launch | Deploy locally/server and switch to "Production" mode. | 🔴 | **P0** | All |
