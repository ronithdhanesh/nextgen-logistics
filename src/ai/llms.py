from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

load_dotenv()

def get_llm():
    llm = ChatGoogleGenerativeAI(
        model="gemini-flash-latest",
        api_key=os.getenv("GOOGLE_API_KEY")
    )

    return llm

# llm = get_llm()
# print(llm.invoke("what is the capital of france"))