import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain

from embed_store import chroma_vectordb
from prompt import PROMPT
from logger import logging


load_dotenv()
GOOGLE_GEMINI_API = os.getenv("GOOGLE_GEMINI_API")


llm = GoogleGenerativeAI(model="gemini-pro", api_key=GOOGLE_GEMINI_API)
logging.info("LLM defined successfully.")


retriever = chroma_vectordb.as_retriever(search_kwargs={'k': 2})
logging.info("Retriever initialized successfully.")


question_answer_chain = create_stuff_documents_chain(llm=llm, prompt=PROMPT)
qa_chain = create_retrieval_chain(retriever=retriever, combine_docs_chain=question_answer_chain)
logging.info("QA chain created successfully.")