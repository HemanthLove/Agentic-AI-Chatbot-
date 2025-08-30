# set up API keys for groq and Tavily
import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()
GROQ_API_KEY=os.environ.get("GROQ_API_KEY")
TAVILY_API_KEY=os.environ.get("TAVILY_API_KEY")
OPENAI_API_KEY=os.environ.get("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)
# # set up LLM and tools
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults

openai_llm = ChatOpenAI(model="gpt-4o")
groq_llm= ChatGroq(model= "llama-3.3-70b-versatile")

from langgraph.prebuilt import create_react_agent
from langchain_core.messages.ai import AIMessage

def get_response_from_ai_agent(llm_id , query , allow_search , system_prompt , provider):
    if provider=="Groq":
        llm=ChatGroq(model=llm_id)
    elif provider =="OpenAI":
        llm=ChatOpenAI(model=llm_id)
    
    tools= [TavilySearchResults(max_results=2)] if allow_search else []
        
    agent = create_react_agent(
    model=llm,
    tools=tools
    )

    messages_list =[]
  
    if system_prompt:
     messages_list.append({"role": "system", "content": system_prompt})
    for msg in query:
     messages_list.append({"role": "user", "content": msg})

    response = agent.invoke({"messages": messages_list})

# Extract the answer from the agent's response
    answer = None
    if "messages" in response and isinstance(response["messages"], list):
     for msg in response["messages"]:
        # If the message is an object with "content" and is an AIMesssage-type
        if hasattr(msg, "content") and (
            hasattr(msg, "type") and "AIMessage" in str(type(msg))
        ):
            answer = msg.content
        # OR if it's a dict with role "assistant" or "ai"
        elif isinstance(msg, dict):
            if msg.get("role") in ("assistant", "ai"):
                answer = msg.get("content")
# Fallback: try to get content from a different location (sometimes response itself has `.content`)
    if not answer and hasattr(response, "content"):
     answer = response.content

# ALWAYS return just the answer as a JSON dict
    return  answer or "Could not extract answer."





   




