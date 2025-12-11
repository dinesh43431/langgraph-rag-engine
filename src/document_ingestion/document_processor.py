from typing import List, Union
from pathlib import Path

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from langchain_community.document_loaders import (
    WebBaseLoader,
    PyPDFLoader,
    TextLoader,
    PyPDFDirectoryLoader,
)


class DocumnetProcessor:   # keep the name you used elsewhere
    def __init__(self, chunk_size: int = 500, chunk_overlap: int = 50):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
        )

    def load_from_url(self, url: str) -> List[Document]:
        loader = WebBaseLoader(url)
        return loader.load()

    def load_from_pdf_dir(self, directory: Union[str, Path]) -> List[Document]:
        loader = PyPDFDirectoryLoader(str(directory))
        return loader.load()

    def load_from_txt(self, file_path: Union[str, Path]) -> List[Document]:
        loader = TextLoader(str(file_path), encoding="utf-8")
        return loader.load()

    def load_from_pdf(self, file_path: Union[str, Path]) -> List[Document]:
        loader = PyPDFLoader(str(file_path))
        return loader.load()

    def load_documnents(self, sources: List[Union[str, Path]]) -> List[Document]:
        """Load docs from URLs, dirs, .txt, or .pdf paths passed in `sources`."""
        docs: List[Document] = []

        for src in sources:
            # normalize src to string + Path
            if isinstance(src, Path):
                src_str = str(src)
                path = src
            else:
                src_str = src
                path = Path(src_str)

            # URL
            if src_str.startswith("http://") or src_str.startswith("https://"):
                docs.extend(self.load_from_url(src_str))
            # directory (e.g. "data")
            if path.is_dir():
                docs.extend(self.load_from_pdf_dir(path))
            # .txt file
            elif path.suffix.lower() == ".txt":
                loader = TextLoader(str(path), encoding="utf-8")
                if str(loader).startswith("http://") or str(loader).startswith("https://"):
                    docs.extend(self.load_from_url(src_str))
                else:
                    docs.extend(self.load_from_txt(path))
            # .pdf file
            elif path.suffix.lower() == ".pdf":
                docs.extend(self.load_from_pdf(path))
            else:
                raise ValueError(f"Unsupported source type: {src}")

        return docs

    def split_documentss(self, documents: List[Document]) -> List[Document]:
        """Split documents into chunks."""
        return self.splitter.split_documents(documents)

    def process_url(self, urls: List[Union[str, Path]]) -> List[Document]:
        """Main entry: load from sources then split into chunks."""
        docs = self.load_documnents(urls)
        return self.split_documentss(docs)
