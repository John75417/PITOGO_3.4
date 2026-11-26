from collections import deque

graph = {
    'P': ['I'],
    'I': ['P', 'T'],
    'T': ['I', 'O'],
    'O': ['T', 'G'],
    'G': ['O', 'O2'],
    'O2': ['G']
}

def BFS(graph, start):
    visited = set()
    queue = deque([start])

    visited.add(start)

    while queue:
        vertex = queue.popleft()

        print(vertex.replace("O2", "O"), end=" ")

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

print("Graph - BFS")
BFS(graph, 'P')