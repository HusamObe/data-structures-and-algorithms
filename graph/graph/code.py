class Graph:
    def __init__(self):
        self.vertices = {}
    
    def add_vertex(self, value):
        if value not in self.vertices:
            self.vertices[value] = []
    
    def add_edge(self, vertex1, vertex2, weight=None):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.vertices[vertex1].append((vertex2, weight))
            self.vertices[vertex2].append((vertex1, weight))
    
    def get_vertices(self):
        return list(self.vertices.keys())
    
    def get_neighbors(self, vertex):
        if vertex in self.vertices:
            return self.vertices[vertex]
    
    def size(self):
        return len(self.vertices)


if __name__ == "__main__":
    graph = Graph()

    
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")

    
    graph.add_edge("A", "B", weight=3)
    graph.add_edge("B", "C", weight=2)
    graph.add_edge("A", "C", weight=4)

    vertices = graph.get_vertices()
    print("Vertices:", vertices)

    neighbors = graph.get_neighbors("A")
    print("Neighbors of A:", neighbors)

    graph_size = graph.size()
    print("Graph size:", graph_size)
