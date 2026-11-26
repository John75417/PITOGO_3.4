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

# DFS Preorder
def DFS(root):
    if root is None:
        return

    print(root.data, end=" ")
    DFS(root.left)
    DFS(root.right)

print("Binary Tree - DFS (Preorder)")
DFS(root)