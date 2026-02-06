"""Test suite for Project 48"""

import pytest
from exercise import create_few_shot_prompt, create_chain_of_thought_prompt


def test_few_shot_prompt():
    examples = [("2+2", "4"), ("3+3", "6")]
    prompt = create_few_shot_prompt(examples, "4+4")
    assert "4+4" in prompt
    assert len(prompt) > 0


def test_chain_of_thought():
    prompt = create_chain_of_thought_prompt("Solve: 5+3")
    assert len(prompt) > 0
