"""Test suite for Project 46"""

import pytest
from exercise import RAGSystem


def test_rag_system():
    # Mock retriever and generator for testing
    class MockRetriever:
        def retrieve(self, query, top_k=5):
            return ["doc1", "doc2"]
    
    class MockGenerator:
        def generate(self, prompt):
            return "answer"
    
    rag = RAGSystem(MockRetriever(), MockGenerator())
    context = rag.retrieve("query")
    assert len(context) > 0
