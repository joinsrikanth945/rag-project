"""
Configuration management for RAG System
"""

from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """
    Application settings
    """
    # FastAPI
    APP_NAME: str = "Agentic RAG System"
    DEBUG: bool = True
    LOG_LEVEL: str = "INFO"
    
    # Server
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    
    # Document Processing
    CHUNK_SIZE: int = 1000
    CHUNK_OVERLAP: int = 200
    TOP_K_CHUNKS: int = 5
    
    # Vector Store
    VECTOR_STORE_TYPE: str = "azure_search"  # or "chroma"
    
    # Azure Services
    AZURE_OPENAI_API_KEY: Optional[str] = None
    AZURE_OPENAI_ENDPOINT: Optional[str] = None
    AZURE_OPENAI_DEPLOYMENT_NAME: str = "gpt-4-turbo"
    AZURE_OPENAI_EMBEDDING_DEPLOYMENT: str = "text-embedding-3-small"
    AZURE_OPENAI_API_VERSION: str = "2024-02-15-preview"
    
    # Azure Cognitive Search
    AZURE_SEARCH_ENDPOINT: Optional[str] = None
    AZURE_SEARCH_API_KEY: Optional[str] = None
    AZURE_SEARCH_INDEX_NAME: str = "rag-index"
    
    # Azure Storage
    AZURE_STORAGE_ACCOUNT_NAME: Optional[str] = None
    AZURE_STORAGE_ACCOUNT_KEY: Optional[str] = None
    AZURE_STORAGE_CONTAINER_NAME: str = "documents"
    
    # LLM
    LLM_TEMPERATURE: float = 0.7
    LLM_MAX_TOKENS: int = 2000
    
    # Document types to support
    SUPPORTED_DOCUMENT_TYPES: list = [
        "pdf", "docx", "xlsx", "txt", "csv"
    ]
    
    class Config:
        env_file = ".env"
        case_sensitive = True


# Global settings instance
settings = Settings()
