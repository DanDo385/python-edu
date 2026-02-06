"""Test suite for Project 43"""

import pytest
import torch
from exercise import LanguageModel


def test_language_model():
    model = LanguageModel(vocab_size=1000, d_model=128)
    x = torch.randint(0, 1000, (4, 10))
    output = model(x)
    assert output is not None
