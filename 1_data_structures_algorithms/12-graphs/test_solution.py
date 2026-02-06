"""Test suite for Project 14: Graphs"""
import pytest
from exercise import Graph

def test_add_edge():
    g = Graph()
    g.add_edge(0, 1)
    assert 1 in g.graph.get(0, [])
    assert 0 in g.graph.get(1, [])

def test_dfs():
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    result = g.dfs(0)
    assert 0 in result
    assert len(result) == 4

def test_bfs():
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    result = g.bfs(0)
    assert result[0] == 0
    assert len(result) == 4

