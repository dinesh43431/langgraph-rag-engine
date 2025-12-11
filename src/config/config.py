# """Configuration module for Agentic RAG system"""

# import os
# from dotenv import load_dotenv
# from langchain_community.chat_models import ChatOllama  # <<< IMPORTANT

# # Load environment variables
# load_dotenv()

# class Config:
#     """Configuration class for RAG system"""

#     # Use FREE local model via Ollama
#     LLM_MODEL = "llama3"   # <-- no "ollama:" prefix here

#     # Document Processing
#     CHUNK_SIZE = 500
#     CHUNK_OVERLAP = 50

#     # Default URLs
#     DEFAULT_URLS = [
#         "https://lilianweng.github.io/posts/2023-06-23-agent/",
#         "https://lilianweng.github.io/posts/2024-04-12-diffusion-video/"
#     ]
    
#     @classmethod
#     def get_llm(cls):
#         """Initialize and return the local Ollama LLM"""
#         return ChatOllama(model=cls.LLM_MODEL)


from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()

class Config:
    LLM_MODEL = "mistralai/devstral-2512:free"

    # Document Processing
    CHUNK_SIZE = 500
    CHUNK_OVERLAP = 50


    @classmethod
    def get_llm(cls):
        return init_chat_model(
            cls.LLM_MODEL,
            model_provider="openai",   # ✅ REQUIRED
            base_url="https://openrouter.ai/api/v1",
        )

