🚀 LangGraph AI Agent

Create intelligent AI agents powered by Groq & OpenAI with an interactive Streamlit UI and robust FastAPI backend.
Supports custom system prompts, multi-model selection, and optional web search for smarter, context-aware responses.

✨ Features

🤖 Multi-Model Support – Groq (LLaMA, Mixtral) & OpenAI (GPT-4o-mini).

🔎 Web Search Integration – Enhance responses with Tavily-powered search.

⚡ FastAPI Backend – Lightweight API for handling AI queries.

🎨 Streamlit Frontend – Clean, user-friendly chat interface.

🛠️ Custom Prompts – Define behavior & role of your AI agent.

📦 Installation

Clone the repository and install dependencies:

git clone https://github.com/your-username/langgraph-ai-agent.git
cd langgraph-ai-agent
pip install -r requirements.txt


Set up your API keys in a .env file:

OPENAI_API_KEY=your_openai_key
GROQ_API_KEY=your_groq_key
TAVILY_API_KEY=your_tavily_key

🚀 Usage
1️⃣ Start the backend (FastAPI):
uvicorn backend:app --reload --host 127.0.0.1 --port 5008

2️⃣ Launch the frontend (Streamlit):
streamlit run frontend.py


Open your browser at http://localhost:8501
 and start chatting!

🤝 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to fork the repo and submit PRs.

📜 License

This project is licensed under the MIT License.
