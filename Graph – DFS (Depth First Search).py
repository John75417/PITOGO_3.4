graph = {
    'P': ['I'],
    'I': ['P', 'T'],
    'T': ['I', 'O'],
    'O': ['T', 'G'],
    'G': ['O', 'O2'],
    'O2': ['G']
}

def DFS(graph, vertex, visited=None):
    if visited is None:
        visited = set()

    visited.add(vertex)

    print(vertex.replace("O2", "O"), end=" ")

    for neighbor in graph[vertex]:
        if neighbor not in visited:
            DFS(graph, neighbor, visited)

print("Graph - DFS")
DFS(graph, 'P')