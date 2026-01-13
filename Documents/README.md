# 🎙️ Real-Time E-Commerce Voicebot using LiveKit  
## Boston Institute – GenAI & Agentic AI Capstone  

---

## 📌 Project Overview

- This project implements a **real-time, AI-powered voice assistant for an e-commerce platform**. Customers can speak naturally through their microphone and receive spoken responses about **products, orders, delivery, returns, and store policies**.

- The system combines LiveKit WebRTC for low-latency audio streaming, a Python-based LiveKit Agent for AI reasoning, and tool-based retrieval (MCP) for accurate access to structured e-commerce data.

- Unlike traditional chatbots, this assistant operates entirely through live voice, creating a realistic customer-support experience.

- **LiveKit WebRTC** for low-latency audio streaming  
- A **Python-based LiveKit Agent** for reasoning and orchestration  
- **GPT-4o Realtime** for speech-to-text, reasoning, and text-to-speech  
- **MCP (Model Context Protocol) tools** for accessing real store data  

---

## 🎯 Capstone Objectives Covered

| Boston Requirement | Implementation |
|------------------|----------------|
| Real-time voice interaction | LiveKit WebRTC + React frontend |
| STT → LLM → TTS | GPT-4o Realtime |
| LLM-driven conversation | System-prompted AI Agent |
| Backend decision logic | MCP tools |
| RAG / factual consistency | Tool-based retrieval from CSV |
| Safety & UX | ID validation, refusal rules |

---

## 🧠 Real-Time System Architecture

```
User Microphone
        ↓
LiveKit WebRTC (Browser)
        ↓
LiveKit Cloud
        ↓
Python LiveKit Agent
        ↓
GPT-4o Realtime (STT + Reasoning + TTS)
        ↓
MCP Tool Server (CSV Data)
        ↓
Voice Output to User
```

A **FastAPI Token Server** securely generates LiveKit access tokens so that:
- The browser never sees API secrets  
- Users join the correct room  
- The AI agent attaches to the right session  

---

## 🛠️ Technology Stack

| Layer | Technology |
|------|-----------|
| Frontend | Next.js + LiveKit React |
| Audio Streaming | LiveKit WebRTC |
| AI Agent | LiveKit Agents (Python) |
| LLM | GPT-4o Realtime |
| STT & TTS | LiveKit Realtime Model |
| Backend Tools | FastMCP |
| Token Server | FastAPI |
| Data | CSV datasets (products, orders, deliveries, returns, customers, policies) |

---

## 📂 Project Structure

```
LiveKit-Ecommerce/
│
├── app/
│   ├── backend/
│   │   ├── agent.py                # LiveKit AI agent
│   │   ├── main.py         # FastAPI token server
│   │   └── tools/
│   │       └── ecommerce_server.py # MCP tools
│   │
│   └── frontend/
│       └── (LiveKit React / Next.js app)
│
├── start.bat
└── README.md
```

---

## 🧩 Core Components

### 1️⃣ LiveKit AI Agent (`agent.py`)

The agent connects to LiveKit rooms and manages:
- Audio input and output  
- Transcription  
- LLM interaction  
- Tool calling  
- Spoken responses  

It uses a system prompt that enforces:
- Short, voice-friendly responses  
- Mandatory tool usage for factual queries  
- Safety rules for unsupported actions  

---

### 2️⃣ MCP Tool Server (`ecommerce_server.py`)

This server exposes deterministic backend tools:

| Tool | Purpose |
|------|--------|
| `get_product(product_id)` | Product details |
| `get_order_status(order_id)` | Order tracking |
| `get_delivery_status(tracking_number)` | Delivery updates |
| `get_return_status(order_id)` | Returns & refunds |
| `get_customer_orders(customer_id)` | Customer purchase history |
| `get_store_policies()` | Delivery, return, and refund rules |

All tools read from CSV datasets, ensuring zero hallucinations.

---

### 3️⃣ RAG Strategy

Instead of embeddings, this project uses tool-based RAG:

```
User → LLM → MCP Tool → Real Data → LLM → Voice
```

This guarantees:
- Accurate answers  
- No hallucinated order or product data  
- Real-time factual consistency  

This approach is ideal for e-commerce systems.

---

### 4️⃣ FastAPI Token Server (`main.py`)

The token server:
- Uses LiveKit API keys  
- Generates short-lived JWT tokens  
- Assigns a UUIDv4 identity to each user  

This ensures:
- Secure authentication  
- Correct agent-to-user mapping  
- No API secrets in the browser  

---

## 🛡️ Safety & UX

The assistant:
- Never guesses product or order data  
- Requests missing IDs politely  
- Refuses actions like payments or cancellations  
- Explains limitations clearly  

This satisfies Boston’s Safety & UX requirement.

---

## ▶️ How to Run

### Create a `.env` file in `app/backend`

```
LIVEKIT_API_KEY=your_key
LIVEKIT_API_SECRET=your_secret
LIVEKIT_URL=wss://your-livekit-url
OPENAI_API_KEY=your_openai_key
```

---

### Install dependencies

**Backend (Python)**
```
livekit
livekit-agents
livekit-plugins-openai
livekit-plugins-silero
livekit-plugins-google
livekit-plugins-noise-cancellation
mem0ai
langchain
langchain-community
langchain-core
langgraph
langgraph-supervisor
python-dotenv
requests
fastapi
flask
streamlit
openai 
groq
langchain-groq 
langchain-tavily
uvicorn
langchain-openai
```

**Frontend**
```
cd app/frontend
pnpm install
```

---

### Run everything
```
start.bat
```

Open:
```
http://localhost:3000
```

Click **Start Call** and begin speaking.

---

## 🧪 Demo Voice Prompts

```
Tell me about product P1002  
Where is my order O9002  
What is your return policy  
Where is my order
```

These show:
- Product lookup  
- Backend order tracking  
- RAG (store policies)  
- UX handling for missing IDs  

---

## 📈 Limitations

- No user login or authentication  
- No real payment or inventory APIs  
- CSV-based data storage  
- English-only voice  

---

## 🚀 Future Improvements

- Database integration  
- Customer accounts  
- Real payment and shipping APIs  
- Multilingual voice support  
- Analytics and monitoring  

---

## 👨‍💻 Author

**Mokshagna Padmasale**  
Associate Software Engineer  
Boston Institute – GenAI & Agentic AI Capstone  
