
from typing import List
from pydantic import BaseModel
from langchain_core.documents import Document

class RAGState((BaseModel)):
     question : str
     retrieved_docs : list[Document]=[]
     answer: str = ""