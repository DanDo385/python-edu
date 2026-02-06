"""Test suite for Project 49"""

import pytest
import torch
from exercise import compute_bleu, compute_perplexity


def test_bleu():
    ref = ["the", "cat", "sat", "on", "the", "mat"]
    cand = ["the", "cat", "sat", "on", "the", "mat"]
    score = compute_bleu(ref, cand)
    assert 0 <= score <= 1


def test_perplexity():
    log_probs = torch.tensor([-0.5, -0.3, -0.4])
    perplexity = compute_perplexity(log_probs)
    assert perplexity > 0
