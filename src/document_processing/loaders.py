"""
Document loading utilities
"""

import logging
from pathlib import Path
from typing import List, Dict, Any

logger = logging.getLogger(__name__)


class DocumentLoader:
    """Load documents from various sources"""
    
    def __init__(self):
        self.supported_formats = [".pdf", ".docx", ".xlsx", ".txt", ".csv"]
        logger.info("DocumentLoader initialized")
    
    def load_documents(self, path: str) -> List[Dict[str, Any]]:
        """
        Load documents from a directory
        
        Args:
            path: Path to directory containing documents
            
        Returns:
            List of loaded documents
        """
        documents = []
        path_obj = Path(path)
        
        if not path_obj.exists():
            logger.warning(f"Path does not exist: {path}")
            return documents
        
        for file in path_obj.iterdir():
            if file.suffix.lower() in self.supported_formats:
                try:
                    doc = self._load_single_file(file)
                    documents.append(doc)
                    logger.info(f"Loaded: {file.name}")
                except Exception as e:
                    logger.error(f"Error loading {file.name}: {str(e)}")
        
        return documents
    
    def _load_single_file(self, file_path: Path) -> Dict[str, Any]:
        """Load a single file"""
        return {
            "source": str(file_path),
            "content": f"Content from {file_path.name}",
            "type": file_path.suffix.lower()
        }
