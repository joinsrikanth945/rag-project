"""
Agentic RAG System - FastAPI Application
Query your 9 PDF files - Shows TOP 1 with 3-5 lines
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List
import logging

from src.document_processing.pdf_loader import PDFLoader

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ============ INITIALIZE FASTAPI APP ============
app = FastAPI(
    title="Agentic RAG System",
    description="Query your 9 PDF documents",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize PDF loader
pdf_loader = PDFLoader()
app.state.documents = []


# ============ PYDANTIC MODELS ============

class QueryRequest(BaseModel):
    question: str


class QueryResponse(BaseModel):
    status: str
    question: str
    answer: str
    sources: Optional[List[str]] = None


# ============ STARTUP EVENT ============

@app.on_event("startup")
async def load_documents():
    """Load PDFs when server starts"""
    print("\n" + "=" * 50)
    print("LOADING YOUR 9 PDF FILES...")
    print("=" * 50)

    documents = pdf_loader.load_pdfs("documents")
    app.state.documents = documents

    print("=" * 50)
    print(f"✓ Ready to query {len(documents)} PDFs!")
    print("=" * 50 + "\n")


# ============ HELPER FUNCTIONS ============

def extract_relevant_lines(content: str, question: str, num_lines: int = 5) -> str:
    """
    Extract 3-5 lines from content that match the question keywords
    """
    question_words = set(question.lower().split())
    lines = content.split('\n')

    # Find lines that contain question keywords
    matching_lines = []
    for line in lines:
        line_lower = line.lower()
        if any(word in line_lower for word in question_words):
            if line.strip():  # Skip empty lines
                matching_lines.append(line.strip())

    # If we found matching lines, use them. Otherwise use first few lines
    if matching_lines:
        return '\n'.join(matching_lines[:num_lines])
    else:
        # Use first 5 lines if no keyword matches
        relevant_lines = [line.strip() for line in lines if line.strip()]
        return '\n'.join(relevant_lines[:num_lines])


# ============ API ENDPOINTS ============

@app.get("/health")
async def health_check():
    """Health check - shows document count"""
    doc_count = len(app.state.documents)
    return {
        "status": "healthy",
        "documents_loaded": doc_count,
        "message": f"Ready to query {doc_count} PDFs"
    }


@app.get("/")
async def root():
    """Welcome endpoint"""
    doc_count = len(app.state.documents)
    return {
        "message": "Welcome to RAG System",
        "pdfs_loaded": doc_count,
        "docs_url": "http://localhost:8000/docs",
        "try_query": "POST /query with your question"
    }


@app.post("/query", response_model=QueryResponse)
async def query_rag(request: QueryRequest):
    """
    Query your 9 PDFs - Returns TOP 1 match with 3-5 lines ONLY

    Example:
    {
      "question": "how to change password in channels"
    }
    """
    try:
        if not request.question or request.question.strip() == "":
            return QueryResponse(
                status="error",
                question=request.question,
                answer="",
                sources=[]
            )

        documents = app.state.documents

        if not documents:
            return QueryResponse(
                status="error",
                question=request.question,
                answer="No documents loaded",
                sources=[]
            )

        # Simple search: find documents with matching keywords
        question_words = request.question.lower().split()
        relevant_docs = []

        for doc in documents:
            content = doc.get("content", "").lower()
            matches = sum(1 for word in question_words if word in content)

            if matches > 0:
                relevant_docs.append({
                    "source": doc["source"],
                    "content": doc["content"],  # Full content for extraction
                    "matches": matches,
                    "pages": doc.get("pages", 0)
                })

        # Sort by matches
        relevant_docs.sort(key=lambda x: x["matches"], reverse=True)
        relevant_docs = relevant_docs[:1]  # TOP 1 ONLY

        # Create answer with LIMITED LINES (3-5 lines)
        if relevant_docs:
            doc = relevant_docs[0]  # Get the top 1
            sources = [doc["source"]]

            # Extract only 3-5 lines
            extracted_content = extract_relevant_lines(doc["content"], request.question, num_lines=5)

            answer = f"📄 Source: {doc['source']} ({doc['pages']} pages)\n"
            answer += f"🔍 Matches: {doc['matches']} keyword(s)\n"
            answer += f"\n{extracted_content}"
        else:
            answer = "❌ No PDFs found matching your question. Try different keywords."
            sources = []

        logger.info(f"Query: {request.question} → Found {len(relevant_docs)} PDF")

        return QueryResponse(
            status="success",
            question=request.question,
            answer=answer,
            sources=sources
        )

    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return QueryResponse(
            status="error",
            question=request.question,
            answer=f"Error: {str(e)}",
            sources=[]
        )


@app.get("/documents")
async def list_documents():
    """List all loaded PDFs"""
    docs = []
    for doc in app.state.documents:
        docs.append({
            "name": doc["source"],
            "pages": doc.get("pages", 0),
            "type": doc.get("type", "pdf")
        })

    return {
        "total": len(docs),
        "documents": docs
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)