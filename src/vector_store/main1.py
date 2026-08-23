@app.post("/query", response_model=QueryResponse)
async def query_rag(request: QueryRequest):
    """
    Query your 9 PDFs - Returns TOP 1 match with full content

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
                    "content": doc["content"],  # FULL CONTENT
                    "matches": matches,
                    "pages": doc.get("pages", 0)
                })

        # Sort by matches
        relevant_docs.sort(key=lambda x: x["matches"], reverse=True)
        relevant_docs = relevant_docs[:1]  # TOP 1 ONLY

        # Create answer
        if relevant_docs:
            doc = relevant_docs[0]  # Get the top 1
            sources = [doc["source"]]

            answer = f"📄 Found in: {doc['source']} ({doc['pages']} pages)\n\n"
            answer += f"📊 Matching keywords: {doc['matches']} match(es)\n\n"
            answer += f"📝 Content:\n\n"
            answer += f"{doc['content']}"  # FULL CONTENT
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