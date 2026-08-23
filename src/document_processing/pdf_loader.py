"""
Simple PDF Loader for 9 PDF files
"""

from pathlib import Path
from typing import List, Dict
import logging

try:
    import PyPDF2
except:
    print("PyPDF2 not installed. Installing...")

logger = logging.getLogger(__name__)


class PDFLoader:
    """Load PDF files"""

    def load_pdfs(self, documents_dir: str) -> List[Dict]:
        """Load all PDFs from documents folder"""
        documents = []
        path = Path(documents_dir)

        if not path.exists():
            logger.warning(f"Documents folder not found: {documents_dir}")
            return documents

        # Find all PDF files
        pdf_files = list(path.glob("*.pdf"))
        print(f"\n📄 Found {len(pdf_files)} PDF files:")

        for pdf_file in pdf_files:
            try:
                print(f"  Loading: {pdf_file.name}...", end=" ")

                content = ""
                with open(pdf_file, 'rb') as f:
                    pdf_reader = PyPDF2.PdfReader(f)
                    num_pages = len(pdf_reader.pages)

                    # Extract text from all pages
                    for page_num in range(num_pages):
                        page = pdf_reader.pages[page_num]
                        content += page.extract_text()

                # Store document
                documents.append({
                    "source": pdf_file.name,
                    "type": "pdf",
                    "content": content,
                    "pages": len(pdf_reader.pages),
                    "path": str(pdf_file)
                })

                print(f"✓ ({num_pages} pages)")

            except Exception as e:
                print(f"✗ Error: {e}")
                logger.error(f"Error loading {pdf_file.name}: {e}")

        print(f"\n✓ Successfully loaded {len(documents)} PDFs\n")
        return documents