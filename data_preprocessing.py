# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader

# def load_pdf(data):
#     loader = DirectoryLoader(data, glob="*.pdf", loader_cls=PyPDFLoader)
#     documents = loader.load()
#     return documents

# # Text chunks
# def text_split(extracted_data):
#     text_splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)
#     text_chunks = text_splitter.split_documents(extracted_data)
#     return text_chunks


from logger import logging
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader


def load_pdf(data):
    logging.info(f"Loading PDFs from directory: {data}")
    loader = DirectoryLoader(data, glob="*.pdf", loader_cls=PyPDFLoader)
    documents = loader.load()
    return documents

# Text chunks
def text_split(extracted_data):
    logging.info("Splitting extracted text into chunks.")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)
    text_chunks = text_splitter.split_documents(extracted_data)
    return text_chunks