from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Create Binary Tree
root = Node('P')
root.left = Node('I')
root.left.left = Node('T')
root.left.left.left = Node('O')
root.left.left.left.left = Node('G')
root.left.left.left.left.left = Node('O')

# BFS Traversal
def BFS(root):
    queue = deque([root])

    while queue:
        current = queue.popleft()
        print(current.data, end=" ")

        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)

print("Binary Tree - BFS")
BFS(root)