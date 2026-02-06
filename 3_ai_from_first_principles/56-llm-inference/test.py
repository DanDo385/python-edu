"""Test suite for Project 47"""

import pytest
from exercise import KVCache


def test_kv_cache():
    cache = KVCache()
    cache.set(0, 0, "key", "value")
    result = cache.get(0, 0)
    assert result is not None
