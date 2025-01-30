# from logger import logging
# from langchain_chroma import Chroma
# from langchain_huggingface.embeddings import HuggingFaceEmbeddings

# from data_preprocessing import load_pdf, text_split


# # Extract data from pdf file
# extracted_data = load_pdf("data/")
# print(f"Length of extracted_data : {len(extracted_data)}")

# # Split data in chunks
# text_chunks = text_split(extracted_data)
# print(f"Length of text chunks : {len(text_chunks)}")


# # Download Embedding Model
# def hugging_face_embedding():
#     embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2", show_progress=True)
#     return embedding


# # Initialize embedding model
# embedding = hugging_face_embedding()
# print(embedding)


# persist_directory = "chatbot_db"
# print(persist_directory)

# chroma_vectordb = Chroma.from_documents(documents=text_chunks, embedding=embedding, persist_directory=persist_directory)
# chroma_vectordb = Chroma(persist_directory=persist_directory, embedding_function=embedding)
# print("Store data into chrome VectorDB")





from logger import logging
from langchain_chroma import Chroma
from langchain_huggingface.embeddings import HuggingFaceEmbeddings

from data_preprocessing import load_pdf, text_split

# Extract data from pdf file
logging.info("Starting PDF data extraction.")
extracted_data = load_pdf("data/")
logging.info(f"Length of extracted_data: {len(extracted_data)}")

# Split data in chunks
logging.info("Splitting extracted data into chunks.")
text_chunks = text_split(extracted_data)
logging.info(f"Length of text chunks: {len(text_chunks)}")

# Download Embedding Model
def hugging_face_embedding():
    logging.info("Initializing HuggingFace embedding model.")
    embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2", show_progress=True)
    logging.info("Embedding model initialized successfully.")
    return embedding

# Initialize embedding model
embedding = hugging_face_embedding()
logging.info("Embedding model instance created.")

persist_directory = "chatbot_db"
logging.info(f"Persist directory set to: {persist_directory}")

logging.info("Initializing Chroma VectorDB.")
chroma_vectordb = Chroma.from_documents(documents=text_chunks, embedding=embedding, persist_directory=persist_directory)
chroma_vectordb = Chroma(persist_directory=persist_directory, embedding_function=embedding)
logging.info("Store data into Chroma VectorDB successfully.")
