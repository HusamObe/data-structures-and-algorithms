class Graph:
    def __init__(self):
        """
            Initialize an empty graph with no vertices or edges.
        """
        self.vertices = {}
    
    def add_vertex(self, value):
        """
        Add a vertex with the given value to the graph if it doesn't already exist.

        Args:
            value: The value of the vertex to be added.
        """
        if value not in self.vertices:
            self.vertices[value] = []
    
    def add_edge(self, vertex1, vertex2, weight=None):
        """
        Add an undirected edge between two vertices with an optional weight.

        Args:
            vertex1: The first vertex of the edge.
            vertex2: The second vertex of the edge.
            weight (optional): The weight of the edge.
        """
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.vertices[vertex1].append((vertex2, weight))
            self.vertices[vertex2].append((vertex1, weight))
    
    def get_vertices(self):
        """
        Get a list of all vertices in the graph.

        Returns:
            list: A list of all vertices in the graph.
        """
        return list(self.vertices.keys())
    
    def get_neighbors(self, vertex):
        """
        Get a list of neighboring vertices along with their edge weights for a given vertex.

        Args:
            vertex: The vertex for which to retrieve neighbors.

        Returns:
            list: A list of neighboring vertices and their edge weights.
        """
        if vertex in self.vertices:
            return self.vertices[vertex]
        return []
    
    def size(self):
        """
        Get the number of vertices in the graph.

        Returns:
            int: The number of vertices in the graph.
        """
        return len(self.vertices)
    
    def depth_first(self, start_vertex):
        """
        Perform a depth-first traversal of the graph starting from the given vertex.

        Args:
            start_vertex: The vertex to start the traversal from.

        Returns:
            list: A list of vertices in the order of their pre-order depth-first traversal.
        """
        visited = set()
        traversal_result = []

        def dfs(vertex):
            visited.add(vertex)
            traversal_result.append(vertex)

            for neighbor, _ in self.vertices[vertex]:
                if neighbor not in visited:
                    dfs(neighbor)

        dfs(start_vertex)
        return traversal_result
    
def business_trip(graph, cities):
    """
    Calculate the total cost of traveling between the given list of cities using the provided graph.

    Args:
        graph (Graph): The graph representing the cities and their connections.
        cities (list): A list of cities to travel through.
        
    Returns:
        int or None: The total cost of traveling through the cities if the path is valid, or None if the path is invalid.
    """
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
    # graph = Graph()

    # graph.add_vertex("Amman")
    # graph.add_vertex("Irbid")
    # graph.add_vertex("Aqaba")

    # graph.add_edge("Amman", "Irbid", weight=20)
    # graph.add_edge("Irbid", "Aqaba", weight=15)
    # graph.add_edge("Aqaba", "Amman", weight=25)

    # cities = ["Amman", "Irbid", "Aqaba"]
    # total_cost = business_trip(graph, cities)
    # if total_cost is None:
    #     print("flight not available")
    # else:
    #     print(f"Trip Total cost: Jd{total_cost}")
        
        
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
    print(", ".join(traversal_result))