import pytest
from graph.code import Graph,business_trip


def test_add_vertex():
    graph = Graph()
    graph.add_vertex('A')
    graph.add_vertex('B')
    graph.add_vertex('C')

    vertices = graph.get_vertices()
    assert 'A' in vertices
    assert 'B' in vertices
    assert 'C' in vertices


def test_add_edge():
    graph = Graph()
    graph.add_vertex('A')
    graph.add_vertex('B')
    graph.add_vertex('C')
    graph.add_edge('A', 'B', weight=10)
    graph.add_edge('B', 'C', weight=15)

    neighbors_a = graph.get_neighbors('A')
    neighbors_b = graph.get_neighbors('B')
    neighbors_c = graph.get_neighbors('C')

    assert ('B', 10) in neighbors_a
    assert ('A', 10) in neighbors_b
    assert ('C', 15) in neighbors_b
    assert ('B', 15) in neighbors_c


def test_depth_first():
    graph = Graph()
    graph.add_vertex('A')
    graph.add_vertex('B')
    graph.add_vertex('C')
    graph.add_vertex('D')
    graph.add_vertex('E')
    graph.add_vertex('F')
    graph.add_vertex('G')
    graph.add_vertex('H')

    graph.add_edge('A', 'B')
    graph.add_edge('A', 'C')
    graph.add_edge('B', 'G')
    graph.add_edge('C', 'D')
    graph.add_edge('C', 'E')
    graph.add_edge('E', 'H')
    graph.add_edge('D', 'F')

    start_vertex = 'A'
    traversal_result = graph.depth_first(start_vertex)

    expected_result = ['A', 'B', 'G', 'C', 'D', 'F', 'E', 'H']
    assert traversal_result == expected_result


def test_business_trip_valid_path():
    graph = Graph()
    graph.add_vertex('Amman')
    graph.add_vertex('Irbid')
    graph.add_vertex('Aqaba')
    graph.add_edge('Amman', 'Irbid', weight=20)
    graph.add_edge('Irbid', 'Aqaba', weight=15)
    graph.add_edge('Aqaba', 'Amman', weight=25)

    cities = ['Amman', 'Irbid', 'Aqaba']
    total_cost = business_trip(graph, cities)
    assert total_cost == 35


def test_business_trip_invalid_path():
    graph = Graph()
    graph.add_vertex('Amman')
    graph.add_vertex('Irbid')
    graph.add_vertex('Aqaba')
    graph.add_edge('Amman', 'Irbid', weight=20)
    graph.add_edge('Irbid', 'Aqaba', weight=15)
    graph.add_edge('Aqaba', 'Amman', weight=25)

    cities = ['Amman', 'Zarqa', 'Irbid']
    total_cost = business_trip(graph, cities)
    assert total_cost is None