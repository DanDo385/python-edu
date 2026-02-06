"""Test suite for Project 45"""

import pytest
from exercise import SimpleTokenizer


def test_tokenizer():
    vocab = {'hello': 0, 'world': 1, '<pad>': 2}
    tokenizer = SimpleTokenizer(vocab)
    tokens = tokenizer.encode("hello world")
    assert len(tokens) > 0
    text = tokenizer.decode(tokens)
    assert isinstance(text, str)
