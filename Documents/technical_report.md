# Technical Report  
## Real-Time E-Commerce Voicebot using LiveKit  
**Boston Institute – GenAI & Agentic AI Capstone**  
**Author:** Mokshagna Padmasale  

---

## 1. Problem Overview & Motivation

Modern e-commerce platforms are increasingly required to provide instant, natural, and accessible customer support. Traditional text-based chatbots are limited by typing speed, accessibility constraints, and poor conversational flow. Human call centers, while effective, are expensive and difficult to scale.

This project addresses these challenges by creating a real-time voice-based AI assistant that allows customers to interact using spoken language. The system is designed to behave like a virtual call center agent that can:

- Understand spoken queries  
- Retrieve accurate business data  
- Respond immediately using synthesized speech  

The project scope focuses on post-purchase support and product inquiry, which represents the highest volume of customer-service interactions in real e-commerce systems.

---

## 2. System Design Philosophy

The system was designed around three core principles:

### Real-time interaction  
The user should experience the assistant as a live conversation partner, not a delayed chatbot.

### Factual reliability  
The assistant must never invent product, order, or delivery data.

### Separation of concerns  
AI reasoning, business data, and audio streaming are implemented as separate services to ensure modularity and scalability.

This philosophy led to the adoption of **LiveKit + AI Agent + MCP Tools** as the core architecture.

---

## 3. Detailed Architecture

The system consists of four main layers:

### 3.1 Frontend (Voice Interface)

A web-based interface built using LiveKit React captures microphone audio and plays back synthesized voice responses. The frontend does not contain any business logic or API secrets; it only handles audio and session initiation.

---

### 3.2 Token & Session Layer

A FastAPI server generates short-lived LiveKit JWT tokens. This prevents exposure of API secrets in the browser and allows secure session management. Each user is assigned a UUID-based identity, enabling the agent to track and manage individual participants.

---

### 3.3 AI Agent Layer

The Python LiveKit Agent acts as the orchestrator of the system. It:

- Receives live audio streams  
- Sends them to the LLM  
- Executes tool calls  
- Returns synthesized voice  

The agent enforces system prompts and decision logic.

---

### 3.4 Data & Tool Layer

Structured e-commerce data is stored in CSV files and exposed through MCP tools. These tools behave like internal APIs that the LLM can call.

---

## 4. Real-Time Processing Pipeline

When a user speaks, the following steps occur:

1. Audio is captured in the browser and streamed via WebRTC  
2. LiveKit routes the audio to the AI agent  
3. GPT-4o Realtime transcribes the speech  
4. The LLM processes the request using the system prompt  
5. If data is required, the LLM calls an MCP tool  
6. The tool retrieves data from CSV  
7. The LLM formulates a response  
8. GPT-4o Realtime synthesizes speech  
9. LiveKit streams the audio back  

This closed-loop pipeline enables continuous, low-latency conversation.

---

## 5. Prompt Engineering Strategy

The system prompt defines:

- The assistant’s persona (e-commerce support agent)  
- Voice style (short, friendly, non-technical)  
- Mandatory tool usage rules  
- Safety constraints  

This ensures that the LLM behaves as a deterministic business assistant rather than a generic chatbot.

---

## 6. Tool-Based Retrieval (RAG)

Instead of embeddings, this project uses tool-augmented RAG. The LLM does not “know” order or product data; it must retrieve it through tools.

This guarantees:

- Consistency with the backend  
- No hallucinations  
- Auditable data flow  

This approach is commonly used in enterprise AI systems.

---

## 7. Latency and Real-Time Constraints

GPT-4o Realtime handles STT, reasoning, and TTS in one pipeline, eliminating network hops between models. Combined with LiveKit’s optimized WebRTC streaming, this allows:

- Low round-trip latency  
- Natural conversational timing  
- Minimal jitter or lag  

---

## 8. Safety & Reliability

The system includes:

- Input validation (IDs required)  
- Refusal of sensitive actions  
- Clear user feedback  

These measures ensure trustworthy and predictable behavior.

---

## 9. Limitations

- No real authentication  
- CSV instead of databases  
- No payment processing  
- English-only support  

---

## 10. Future Enhancements

- Database-backed data  
- User accounts  
- Payment & shipping APIs  
- Multilingual support  
- Analytics  

---

## 11. Conclusion

This project demonstrates a production-style AI voice system for e-commerce. It integrates real-time voice streaming, LLM reasoning, and tool-based data access into a single, scalable architecture, fulfilling all requirements of the Boston GenAI & Agentic AI capstone.
