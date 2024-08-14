import heapq

class Graph:
    """Graph data structure, undirected by default."""
    
    def __init__(self):
        """Initialize a graph with an empty dictionary of vertices."""
        self.vertices = {}

    def add_vertex(self, vertex):
        """Add a vertex to the graph."""
        if vertex not in self.vertices:
            self.vertices[vertex] = {}

    def add_edge(self, source, destination, weight):
        """Add an edge between two vertices with a given weight."""
        if source in self.vertices and destination in self.vertices:
            self.vertices[source][destination] = weight
            self.vertices[destination][source] = weight  # For undirected graph

    def get_neighbors(self, vertex):
        """Get the neighbors of a given vertex."""
        if vertex in self.vertices:
            return self.vertices[vertex]
        else:
            return {}

def dijkstra(graph, start):
    """Compute the shortest paths from the start vertex to all other vertices in the graph."""
    distances = {vertex: float('infinity') for vertex in graph.vertices}
    distances[start] = 0
    priority_queue = [(0, start)]
    shortest_path_tree = {}

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph.get_neighbors(current_vertex).items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                shortest_path_tree[neighbor] = current_vertex

    return distances, shortest_path_tree

# Example usage with the first graph:
graph1 = Graph()
graph1.add_vertex('A')
graph1.add_vertex('B')
graph1.add_vertex('C')
graph1.add_edge('A', 'B', 5)
graph1.add_edge('B', 'C', 3)
graph1.add_edge('A', 'C', 10)

distances1, shortest_path_tree1 = dijkstra(graph1, 'A')
print("Graph 1 Distances:", distances1)
print("Graph 1 Shortest Path Tree:", shortest_path_tree1)

# Test with a different graph configuration:
graph2 = Graph()
graph2.add_vertex('A')
graph2.add_vertex('B')
graph2.add_vertex('C')
graph2.add_vertex('D')
graph2.add_edge('A', 'B', 1)
graph2.add_edge('B', 'C', 2)
graph2.add_edge('A', 'C', 4)
graph2.add_edge('C', 'D', 1)

distances2, shortest_path_tree2 = dijkstra(graph2, 'A')
print("Graph 2 Distances:", distances2)
print("Graph 2 Shortest Path Tree:", shortest_path_tree2)