"""
Breadth-First Search (BFS) algorithm

This algorithm is used to traverse or search tree or graph data structures.
It starts from a given node (root or source) and explores all neighboring nodes at the current depth level
before moving on to the next depth level.

Problem:

Calculate the shortest distance from a single source to all other vertices in an unweighted graph using BFS algorithm.

Input: A simple undirected graph with n ≤ 10^3 vertices in adjacency list format.

Output: An array D[1..n] storing the shortest path length from vertex 1 to vertex i (D[1]=0).
If vertex i is unreachable from 1, set D[i] to -1.

Procedure:

1. Read input file
2. Create graph from adjacency list
3. Use BFS algorithm to find the shortest path from vertex 1 to vertex i
4. Output the result
"""

def read_file(path):
    """
    Read input file and create graph from adjacency list
    """
    with open(path, 'r') as f:
        # Read input file line by line
        lines = f.read().split('\n')
        # Remove empty lines
        lines = [line for line in lines if len(line.split()) >= 2]
    
    graph = {}
    
    # Create a set to store all nodes in the graph
    nodes = set()
    for line in lines:
        # Extract two nodes from each line and add to the set
        nodes.add(line.split()[0])
        nodes.add(line.split()[1])
    
    # Initialize graph: assign an empty list to each node
    for node in nodes:
        graph[node] = []
    
    # Create graph from adjacency list
    for line in lines:
        start_node, end_node = line.split()[0], line.split()[1]
        if start_node!= end_node:
            # Add an edge from start node to end node
            graph[start_node].append(end_node)
    
    return graph

def bfs_shortest_path(start_node, end_node, graph):
    """
    Use BFS algorithm to find the shortest path from start node to end node
    """
    queue = deque([start_node])
    visited = set([start_node])
    dist = {start_node: 0}
    
    while queue:
        curr_node = queue.popleft()
        
        if curr_node == end_node:
            # Return the shortest path length if end node is reached
            return dist[curr_node]
        
        for next_node in graph[curr_node]:
            if next_node not in visited:
                # Mark next node as visited and add to the queue
                visited.add(next_node)
                queue.append(next_node)
                dist[next_node] = dist[curr_node] + 1
    # Return -1 if end node is unreachable
    return -1

if __name__ == '__main__':
    from collections import deque
    
    graph = read_file('../test/rosalind_bfs.txt')
    
    D = []
    for end_node in graph:
        # Calculate the shortest path length from vertex 1 to each vertex
        D.append(bfs_shortest_path('1', end_node, graph))
    
    # Output the result
    for n in D:
        print(n, end=' ')
