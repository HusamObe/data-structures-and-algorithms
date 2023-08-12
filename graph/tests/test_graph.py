import pytest
from ...graph.graph.code import Graph

@pytest.fixture
def graph():
    return Graph()

def test_add_vertex(graph):
    graph.add_vertex("A")
    assert "A" in graph.get_vertices()

def test_add_edge(graph):
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_edge("A", "B", weight=3)
    neighbors_of_a = graph.get_neighbors("A")
    neighbors_of_b = graph.get_neighbors("B")
    assert ("B", 3) in neighbors_of_a
    assert ("A", 3) in neighbors_of_b

def test_get_vertices(graph):
    graph.add_vertex("A")
    graph.add_vertex("B")
    vertices = graph.get_vertices()
    assert "A" in vertices
    assert "B" in vertices

def test_get_neighbors(graph):
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_edge("A", "B", weight=2)
    graph.add_edge("A", "C", weight=4)
    neighbors = graph.get_neighbors("A")
    assert ("B", 2) in neighbors
    assert ("C", 4) in neighbors

def test_size(graph):
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    assert graph.size() == 3

def test_single_vertex_edge(graph):
    graph.add_vertex("A")
    graph.add_edge("A", "A", weight=1)
    neighbors = graph.get_neighbors("A")
    assert ("A", 1) in neighbors
    assert len(neighbors) == 1