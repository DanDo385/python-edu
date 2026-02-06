"""Test suite for Project 50"""

import pytest
from exercise import ModelServer


def test_model_server():
    class MockModel:
        def generate(self, text):
            return f"response to {text}"
    
    server = ModelServer(MockModel())
    result = server.predict("test")
    assert isinstance(result, str)


def test_batch_predict():
    class MockModel:
        def generate(self, text):
            return f"response to {text}"
    
    server = ModelServer(MockModel())
    results = server.batch_predict(["test1", "test2"])
    assert len(results) == 2
