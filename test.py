from src.vectorstore.vectorstore import VectorStore
from src.document_ingestion.document_processor import DocumnetProcessor
from src.config.config import Config

# 1. Process the same PDF you used
doc_processor = DocumnetProcessor(
    chunk_size=Config.CHUNK_SIZE,
    chunk_overlap=Config.CHUNK_OVERLAP
)

documents = doc_processor.process_url(["data"]) # adjust to your actual path

# 2. Build vectorstore
vs = VectorStore()
vs.create_vectorstore(documents)

# 3. Test retrieval
retriever = vs.get_retriever()
docs = retriever.invoke("who is india's t20i vice captain")

print("Top doc snippet:\n")
print(docs[0].page_content[:400])
