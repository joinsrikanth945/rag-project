"""
Document chunking utilities
"""

import logging
from typing import List, Dict, Any

logger = logging.getLogger(__name__)


class DocumentChunker:
    """Split documents into chunks"""
    
    def __init__(self, chunk_size: int = 1000, overlap: int = 200):
        self.chunk_size = chunk_size
        self.overlap = overlap
        logger.info(f"DocumentChunker initialized (size={chunk_size}, overlap={overlap})")
    
    def chunk_documents(self, documents: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Split documents into chunks
        
        Args:
            documents: List of documents
            
        Returns:
            List of chunked documents
        """
        chunks = []
        
        for doc in documents:
            content = doc.get("content", "")
            doc_chunks = self._chunk_text(content, doc.get("source", ""))
            chunks.extend(doc_chunks)
        
        logger.info(f"Created {len(chunks)} chunks from {len(documents)} documents")
        return chunks
    
    def _chunk_text(self, text: str, source: str) -> List[Dict[str, Any]]:
        """Chunk a single text"""
        chunks = []
        
        for i in range(0, len(text), self.chunk_size - self.overlap):
            chunk = text[i:i + self.chunk_size]
            if chunk.strip():
                chunks.append({
                    "content": chunk,
                    "source": source,
                    "chunk_id": len(chunks)
                })
        
        return chunks
