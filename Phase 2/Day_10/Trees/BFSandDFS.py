"""
Tree Traversal: BFS and DFS

1. **Breadth-First Search (BFS):**
   - Also known as Level Order Traversal.
   - Visit all nodes level by level, starting from the root.
   - Uses a queue to keep track of the nodes at the current level.

   Example: For the tree:
           1
         /   \
        2     3
       / \
      4   5
   BFS Traversal: 1, 2, 3, 4, 5

2. **Depth-First Search (DFS):**
   - Explores as far as possible along each branch before backtracking.
   - Three types of DFS:
       a. Inorder (Left, Root, Right)  -> Covered earlier
       b. Preorder (Root, Left, Right) -> Covered earlier
       c. Postorder (Left, Right, Root) -> Covered earlier
   - DFS can also be implemented iteratively using a stack.

   Example: DFS Preorder Traversal: 1, 2, 4, 5, 3
"""

from collections import deque

class Node:
    """Class to represent a node in a binary tree."""
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    """Class to represent a binary tree with BFS and DFS methods."""

    def __init__(self):
        self.root = None

    def bfs(self):
        """Perform Breadth-First Search (Level Order Traversal)."""
        if not self.root:
            return

        queue = deque([self.root])
        print("BFS Traversal:", end=" ")
        while queue:
            current = queue.popleft()
            print(current.data, end=" ")

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        print()

    def dfs_iterative(self):
        """Perform Depth-First Search using a stack."""
        if not self.root:
            return

        stack = [self.root]
        print("DFS Iterative Preorder Traversal:", end=" ")
        while stack:
            current = stack.pop()
            print(current.data, end=" ")

            # Push right child first, so the left child is processed first
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
        print()

# Example Usage
if __name__ == "__main__":
    # Creating the binary tree:
    #        1
    #      /   \
    #     2     3
    #    / \
    #   4   5

    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)

    print("Tree Traversals:\n")

    # BFS Traversal
    tree.bfs()

    # DFS Iterative Preorder Traversal
    tree.dfs_iterative()
