from collections import defaultdict, deque
import matplotlib.pyplot as plt
import networkx as nx

class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Number of vertices
        self.graph = defaultdict(dict)  # Adjacency list to store capacities

    def add_edge(self, u, v, capacity_label, capacities):
        # Add forward and backward edges
        self.graph[u][v] = capacities[capacity_label]
        self.graph[v][u] = 0  # Reverse edge with 0 capacity initially

    def bfs(self, source, sink, parent):
        visited = [False] * self.V
        queue = deque([source])
        visited[source] = True

        while queue:
            u = queue.popleft()

            for v, capacity in self.graph[u].items():
                if not visited[v] and capacity > 0:  # Check residual capacity
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u

                    if v == sink:
                        return True

        return False

    def ford_fulkerson(self, source, sink):
        parent = [-1] * self.V  # Array to store the path
        max_flow = 0

        while self.bfs(source, sink, parent):
            # Find the maximum flow through the path found by BFS
            path_flow = float('Inf')
            s = sink

            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            # Update residual capacities in the network
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

            max_flow += path_flow

        return max_flow

    def visualize(self, capacities):
        G = nx.DiGraph()
        for u in self.graph:
            for v, capacity in self.graph[u].items():
                if capacity > 0:
                    G.add_edge(u, v, label=str(capacity))

        pos = nx.spring_layout(G)  # Layout for better visualization
        nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=10, font_weight="bold")
        edge_labels = nx.get_edge_attributes(G, 'label')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color="red")
        plt.title("Graph with Capacities")
        plt.show()


# Input section
x1 = int(input("Enter the capacity for edge (1 -> 2): "))
x2 = int(input("Enter the capacity for edge (1 -> 3): "))
x3 = int(input("Enter the capacity for edge (2 -> 4): "))
x4 = int(input("Enter the capacity for edge (2 -> 5): "))
x5 = int(input("Enter the capacity for edge (3 -> 4): "))
x6 = int(input("Enter the capacity for edge (3 -> 6): "))
x7 = int(input("Enter the capacity for edge (4 -> 5): "))
x8 = int(input("Enter the capacity for edge (4 -> 6): "))
x9 = int(input("Enter the capacity for edge (5 -> 7): "))
x10 = int(input("Enter the capacity for edge (6 -> 7): "))
x11 = int(input("Enter the capacity for edge (2 -> 3): "))
x12 = int(input("Enter the capacity for edge (5 -> 6): "))

# Map variable names to edge labels
capacities = {
    "x1": x1,
    "x2": x2,
    "x3": x3,
    "x4": x4,
    "x5": x5,
    "x6": x6,
    "x7": x7,
    "x8": x8,
    "x9": x9,
    "x10": x10,
    "x11": x11,
    "x12": x12,
}

# Build the graph
g = Graph(8)  # Graph with 8 nodes (1 to 7, plus 0-index padding for simplicity)

g.add_edge(1, 2, "x1", capacities)
g.add_edge(1, 3, "x2", capacities)
g.add_edge(2, 4, "x3", capacities)
g.add_edge(2, 5, "x4", capacities)
g.add_edge(3, 4, "x5", capacities)
g.add_edge(3, 6, "x6", capacities)
g.add_edge(4, 5, "x7", capacities)
g.add_edge(4, 6, "x8", capacities)
g.add_edge(5, 7, "x9", capacities)
g.add_edge(6, 7, "x10", capacities)
g.add_edge(2, 3, "x11", capacities)
g.add_edge(5, 6, "x12", capacities)

# Visualize the graph
g.visualize(capacities)

source = 1  # Source node
sink = 7    # Sink node
print("The maximum possible flow is", g.ford_fulkerson(source, sink))
