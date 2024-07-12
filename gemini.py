import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

# lang smith
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
os.environ["LANGCHAIN_API_KEY"] = os.environ["LANG_SMITH_API_KEY"]
os.environ["LANGCHAIN_PROJECT"] = "vs-code-testing"

# others all env vars
groq_api = "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"
google_api = os.environ["GOOGLE_API_KEY"]

# model loading & result printing
llm = ChatGoogleGenerativeAI(model="gemini-pro")
result = llm.invoke("Write a ballad about LangChain")
print(result.content)


