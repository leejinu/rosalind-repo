"""

Connected Components

Problem:
Ths task is use Depth-First Search(DFS) to compute the number of connected components in a given undirected graph

Given: A simple graph with n <= 10^3 vertices in the edge list format.

Return: The number of connected components in the graph.

Solution)
    1. Initialize all vertices as not visited
    2. Do the following for every vertex v:
        - If v is not visited before, call the DFS. and print the newline character to print each component in a new line
         a. Mark v as visited and print v
         b. For every adjacent u of v, If u is not visited, then recursively call the DFS
"""

def read_file(path):
    with open(path, 'r') as f:
        lines = f.read().split('\n')
        lines = [line for line in lines if len(line.split())>= 2]
    graph = {}

    n = int(lines[0].split()[0])

    lines = lines[1:]
    start_nodes = []
    for line in lines:
        start_nodes.append(int(line.split()[0]))
        start_nodes.append(int(line.split()[1]))

    start_nodes = list(range(1,n+1))
    for node in sorted(start_nodes):
        graph[int(node)] = []
    for line in lines:
        start_node, end_node = int(line.split()[0]),int(line.split()[1])
        if start_node != end_node:
            graph[start_node].append(end_node)
            graph[end_node].append(start_node)

    return graph

def DFS(node, graph, visited, component):
    visited[node] = True
    component.append(node)
    for neighbor in graph[node]:
        if not visited[neighbor]:
            DFS(neighbor, graph, visited, component)
    
def n_connected_components(graph):

    visited = {node: False for node in graph.keys()}
    components = []

    for node in graph.keys():
        if not visited[node]:
            component = []
            DFS(node, graph, visited, component)
            components.append(component)

    return len(components)
            
if __name__ == "__main__":

    graph = {}
    graph = read_file('rosalind_cc.txt')

    print(n_connected_components(graph))

    
