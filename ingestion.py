from pathlib import Path

from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import OpenAIEmbeddings
from tqdm import tqdm

# load environment variables from .env file
load_dotenv()


# load pdfs
# documents = []
# pdf_directory = Path("./papers")

# for pdf_path in tqdm(pdf_directory.glob("*.pdf"), desc="Loading PDFs"):
#     loader = PyPDFLoader(str(pdf_path))
#     documents.extend(loader.load())


# split documents
# print("Splitting documents")
# text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
#     chunk_size=1000, chunk_overlap=200
# )

# doc_splits = text_splitter.split_documents(documents)


# vectorize chunks
# print("Vectorizing chunks")
# vectorstore = Chroma.from_documents(
#     documents=doc_splits,
#     collection_name="food-desert-rag",
#     persist_directory="./.chroma", # save to disk
#     embedding=OpenAIEmbeddings()
# )

# load vectorstore
retriever = Chroma(
    collection_name="food-desert-rag",
    persist_directory="./.chroma",
    embedding_function=OpenAIEmbeddings(),
).as_retriever(
    search_kwargs={
        "k": 20,  # Number of documents to return
    }
)
