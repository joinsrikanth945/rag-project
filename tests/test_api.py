"""
API tests for RAG System
"""

import pytest
from fastapi.testclient import TestClient
from src.main import app


client = TestClient(app)


def test_health_check():
    """Test health check endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["version"] == "1.0.0"


def test_query_valid():
    """Test query with valid input"""
    response = client.post(
        "/query",
        json={"question": "What is RAG?"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert data["question"] == "What is RAG?"
    assert len(data["answer"]) > 0


def test_query_empty():
    """Test query with empty question"""
    response = client.post(
        "/query",
        json={"question": ""}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "error"


def test_root():
    """Test root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
