from typing import List
from langchain_community.vectorstores import FAISS

from langchain_huggingface import HuggingFaceEmbeddings

from langchain_core.documents import Document

class VectorStore:

    def __init__(self):
        
        self.embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        self.vectorstore = None
        self.retriever = None

    # name aligned with your Streamlit: create_vectorstore
    def create_vectorstore(self, documents: List[Document]):
        if not documents:
            raise ValueError("No documents provided to create vectorstore")
        self.vectorstore = FAISS.from_documents(documents, self.embedding)
        self.retriever = self.vectorstore.as_retriever()

    def get_retriever(self):
        if self.retriever is None:
             raise ValueError("Vector Store not initialized")
        return self.retriever

    def retrieve(self, query: str, k: int = 4) -> List[Document]:
        if self.retriever is None:
            raise ValueError("Vector store not initialized")
        docs = self.retriever._get_relevant_documents(query) if hasattr(self.retriever, "get_relevant_documents") \
               else self.retriever.retrieve(query)
        # optionally limit to k
        return docs[:k]
