"""
Tree Traversals in Binary Trees

1. **Inorder Traversal (Left, Root, Right):**
   - Visit the left subtree.
   - Visit the root node.
   - Visit the right subtree.

   Example: For the tree:
           1
         /   \
        2     3
       / \
      4   5
   Inorder Traversal: 4, 2, 5, 1, 3

2. **Preorder Traversal (Root, Left, Right):**
   - Visit the root node.
   - Visit the left subtree.
   - Visit the right subtree.

   Example: Preorder Traversal: 1, 2, 4, 5, 3

3. **Postorder Traversal (Left, Right, Root):**
   - Visit the left subtree.
   - Visit the right subtree.
   - Visit the root node.

   Example: Postorder Traversal: 4, 5, 2, 3, 1
"""

class Node:
    """Class to represent a node in a binary tree."""
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    """Class to represent a binary tree with traversal methods."""
    
    def __init__(self):
        self.root = None

    def inorder_traversal(self, node):
        """Perform Inorder Traversal (Left, Root, Right)."""
        if node:
            self.inorder_traversal(node.left)
            print(node.data, end=" ")
            self.inorder_traversal(node.right)

    def preorder_traversal(self, node):
        """Perform Preorder Traversal (Root, Left, Right)."""
        if node:
            print(node.data, end=" ")
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)

    def postorder_traversal(self, node):
        """Perform Postorder Traversal (Left, Right, Root)."""
        if node:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.data, end=" ")

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

    print("Inorder Traversal (Left, Root, Right):")
    tree.inorder_traversal(tree.root)
    print("\n")

    print("Preorder Traversal (Root, Left, Right):")
    tree.preorder_traversal(tree.root)
    print("\n")

    print("Postorder Traversal (Left, Right, Root):")
    tree.postorder_traversal(tree.root)
    print("\n")
