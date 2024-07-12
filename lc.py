import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

# loading .env file
load_dotenv() 

# lang smith
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
os.environ["LANGCHAIN_API_KEY"] = os.environ["LANG_SMITH_API_KEY"]
os.environ["LANGCHAIN_PROJECT"] = "vs-code-testing"

# others all env vars
GROQ_API_KEY = os.environ["GROQ_API_KEY"]

# model loading
chat = ChatGroq(temperature=0, groq_api_key=GROQ_API_KEY, model_name="mixtral-8x7b-32768")

# prompting
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."), 
        ("human", "{text}")
    ])

# chaining
chain = prompt|chat

# input giving or questioning
result = chain.invoke({"text": "Explain the importance of low latency LLMs. in one line"})
print(result.content)

