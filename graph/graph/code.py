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
    
def business_trip(graph, cities):
    cost = 0

    for i in range(len(cities) - 1):
        if cities[i] not in graph.vertices or cities[i + 1] not in graph.vertices:
            return None  

        found = False
        for neighbor, weight in graph.get_neighbors(cities[i]):
            if neighbor == cities[i + 1]:
                cost += weight
                found = True
                break

        if not found:
            return None 

    return cost


if __name__ == "__main__":
    graph = Graph()

    graph.add_vertex("Amman")
    graph.add_vertex("Irbid")
    graph.add_vertex("Aqaba")

    graph.add_edge("Amman", "Irbid", weight=20)
    graph.add_edge("Irbid", "Aqaba", weight=15)
    graph.add_edge("Aqaba", "Amman", weight=25)

    cities = ["Amman", "Irbid", "Aqaba"]
    total_cost = business_trip(graph, cities)
    if total_cost is None:
        print("flight not available")
    else:
        print(f"Trip Total cost: Jd{total_cost}")