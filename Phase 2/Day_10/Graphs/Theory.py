"""
Graphs in Data Structures

Graphs are a collection of nodes (vertices) connected by edges. They are used to represent relationships in a wide variety of applications like social networks, maps, and network flows.

1. **Graph Terminologies**:
    - Vertex (Node): A fundamental unit of a graph.
    - Edge: A connection between two vertices.
    - Degree: The number of edges connected to a vertex.
    - Path: A sequence of vertices connected by edges.
    - Cycle: A path where the first and last vertices are the same.
    - Connected Graph: All vertices are reachable from any vertex.
    - Disconnected Graph: Some vertices cannot be reached.

2. **Types of Graphs**:
    - **Directed Graph**: Edges have a direction.
    - **Undirected Graph**: Edges have no direction.
    - **Weighted Graph**: Edges have weights (costs).
    - **Unweighted Graph**: Edges do not have weights.
    - **Cyclic Graph**: Contains at least one cycle.
    - **Acyclic Graph**: Does not contain cycles.

3. **Graph Representations**:
    - **Adjacency Matrix**: A 2D array where matrix[i][j] is 1 if there is an edge from vertex i to vertex j.
    - **Adjacency List**: A list where each vertex has a list of connected vertices.

4. **Graph Traversals**:
    - **Breadth-First Search (BFS)**: Level-wise traversal using a queue.
    - **Depth-First Search (DFS)**: Traversal as far as possible along a branch using recursion or a stack.

"""

from collections import defaultdict, deque

class Graph:
    """Graph implementation using adjacency list."""

    def __init__(self, is_directed=False):
        self.graph = defaultdict(list)
        self.is_directed = is_directed

    def add_edge(self, u, v, weight=1):
        """Add an edge to the graph."""
        self.graph[u].append((v, weight))
        if not self.is_directed:
            self.graph[v].append((u, weight))

    def display_adjacency_list(self):
        """Display the adjacency list of the graph."""
        print("Graph (Adjacency List):")
        for vertex, edges in self.graph.items():
            print(f"{vertex} -> {[(neighbor, weight) for neighbor, weight in edges]}")

    def bfs(self, start):
        """Breadth-First Search (BFS)."""
        visited = set()
        queue = deque([start])
        print(f"BFS Traversal (starting from {start}):", end=" ")
        while queue:
            node = queue.popleft()
            if node not in visited:
                print(node, end=" ")
                visited.add(node)
                queue.extend(neighbor for neighbor, _ in self.graph[node] if neighbor not in visited)
        print()

    def dfs_recursive(self, start, visited=None):
        """Depth-First Search (DFS) - Recursive."""
        if visited is None:
            visited = set()
        visited.add(start)
        print(start, end=" ")
        for neighbor, _ in self.graph[start]:
            if neighbor not in visited:
                self.dfs_recursive(neighbor, visited)

    def dfs_iterative(self, start):
        """Depth-First Search (DFS) - Iterative."""
        visited = set()
        stack = [start]
        print(f"DFS Iterative Traversal (starting from {start}):", end=" ")
        while stack:
            node = stack.pop()
            if node not in visited:
                print(node, end=" ")
                visited.add(node)
                stack.extend(neighbor for neighbor, _ in reversed(self.graph[node]) if neighbor not in visited)
        print()


# Example Usage
if __name__ == "__main__":
    """
    Example Graph:
         1 -- 2
         |    |
         4 -- 3
    """

    graph = Graph(is_directed=False)
    graph.add_edge(1, 2)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(4, 3)

    print("\nGraph Theory & Traversals:\n")
    
    # Display Adjacency List
    graph.display_adjacency_list()

    # BFS Traversal
    graph.bfs(1)

    # DFS Recursive Traversal
    print(f"DFS Recursive Traversal (starting from 1):", end=" ")
    graph.dfs_recursive(1)
    print()

    # DFS Iterative Traversal
    graph.dfs_iterative(1)

"""
Key Notes:
1. Graph Representation:
    - Adjacency List is space-efficient for sparse graphs.
    - Adjacency Matrix is easier for dense graphs but uses more space.

2. Applications of Graphs:
    - Networks (e.g., social, computer, transportation).
    - Shortest Path Algorithms (Dijkstra, Bellman-Ford).
    - Connectivity and Flow Problems.

3. BFS vs DFS:
    - BFS explores all neighbors first (level-wise).
    - DFS explores as deep as possible before backtracking.

Output Example:
Graph (Adjacency List):
1 -> [(2, 1), (4, 1)]
2 -> [(1, 1), (3, 1)]
4 -> [(1, 1), (3, 1)]
3 -> [(2, 1), (4, 1)]

BFS Traversal (starting from 1): 1 2 4 3
DFS Recursive Traversal (starting from 1): 1 2 3 4
DFS Iterative Traversal (starting from 1): 1 4 3 2
"""
