from langchain.prompts import ChatPromptTemplate


system_prompt = (
    "Use the following pieces of information to answer to user's question."
    "If you don't know the answer, just say that you don't know, don't try to make up an answer."
    
    "Context: {context}"
)

PROMPT = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}")
    ]
)