"""
Tree Data Structure - Complete Theory and Implementation in Python

A tree is a hierarchical data structure consisting of nodes, with a single root node
at the top and child nodes branching off from the parent nodes.

Key Characteristics of a Tree:
1. Root Node: The topmost node of the tree.
2. Parent and Child Nodes: Each node (except the root) has a parent; nodes connected below are its children.
3. Leaf Nodes: Nodes with no children.
4. Height of Tree: Longest path from the root to a leaf node.
5. Binary Tree: A tree where each node has at most two children (left and right).

Key Operations on a Tree:
1. Traversals:
   a. In-order: Left -> Root -> Right
   b. Pre-order: Root -> Left -> Right
   c. Post-order: Left -> Right -> Root
2. Insertion
3. Deletion
"""

class Node:
    """
    Class to represent a node in a binary tree.
    Each node has:
    - data: The value stored in the node.
    - left: Pointer to the left child.
    - right: Pointer to the right child.
    """
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    """
    Class to represent a binary tree and its operations.
    """
    def __init__(self):
        self.root = None

    def insert(self, data):
        """
        Insert a node into the binary tree using level order traversal.
        Time Complexity: O(n)
        """
        new_node = Node(data)
        if not self.root:
            self.root = new_node
            return

        queue = [self.root]
        while queue:
            temp = queue.pop(0)
            if not temp.left:
                temp.left = new_node
                return
            else:
                queue.append(temp.left)

            if not temp.right:
                temp.right = new_node
                return
            else:
                queue.append(temp.right)

    def in_order_traversal(self, node, result):
        """
        Perform in-order traversal (Left -> Root -> Right).
        Time Complexity: O(n)
        """
        if node:
            self.in_order_traversal(node.left, result)
            result.append(node.data)
            self.in_order_traversal(node.right, result)

    def pre_order_traversal(self, node, result):
        """
        Perform pre-order traversal (Root -> Left -> Right).
        Time Complexity: O(n)
        """
        if node:
            result.append(node.data)
            self.pre_order_traversal(node.left, result)
            self.pre_order_traversal(node.right, result)

    def post_order_traversal(self, node, result):
        """
        Perform post-order traversal (Left -> Right -> Root).
        Time Complexity: O(n)
        """
        if node:
            self.post_order_traversal(node.left, result)
            self.post_order_traversal(node.right, result)
            result.append(node.data)

    def level_order_traversal(self):
        """
        Perform level-order traversal (Breadth-First Search).
        Time Complexity: O(n)
        """
        if not self.root:
            return []

        result = []
        queue = [self.root]

        while queue:
            temp = queue.pop(0)
            result.append(temp.data)
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)

        return result

    def delete(self, data):
        """
        Delete a node from the binary tree.
        Time Complexity: O(n)
        """
        if not self.root:
            print("The tree is empty.")
            return

        # Find the node to delete and the deepest node
        queue = [self.root]
        to_delete = None
        last = None

        while queue:
            last = queue.pop(0)
            if last.data == data:
                to_delete = last
            if last.left:
                queue.append(last.left)
            if last.right:
                queue.append(last.right)

        if to_delete:
            to_delete.data = last.data  # Replace data of the node to delete
            self._delete_deepest(last)  # Delete the deepest node
        else:
            print(f"Node with value {data} not found.")

    def _delete_deepest(self, d_node):
        """
        Helper function to delete the deepest node.
        """
        queue = [self.root]
        while queue:
            temp = queue.pop(0)
            if temp is d_node:
                temp = None
                return
            if temp.right:
                if temp.right is d_node:
                    temp.right = None
                    return
                queue.append(temp.right)
            if temp.left:
                if temp.left is d_node:
                    temp.left = None
                    return
                queue.append(temp.left)


# Demonstrating Tree Operations
if __name__ == "__main__":
    # Create a binary tree
    bt = BinaryTree()

    # Insert nodes into the tree
    bt.insert(10)
    bt.insert(20)
    bt.insert(30)
    bt.insert(40)
    bt.insert(50)
    bt.insert(60)

    # Traversals
    in_order_result = []
    bt.in_order_traversal(bt.root, in_order_result)
    print("In-order Traversal (Left -> Root -> Right):", in_order_result)

    pre_order_result = []
    bt.pre_order_traversal(bt.root, pre_order_result)
    print("Pre-order Traversal (Root -> Left -> Right):", pre_order_result)

    post_order_result = []
    bt.post_order_traversal(bt.root, post_order_result)
    print("Post-order Traversal (Left -> Right -> Root):", post_order_result)

    print("Level-order Traversal (Breadth-First):", bt.level_order_traversal())

    # Delete a node
    print("\nDeleting node 40...")
    bt.delete(40)
    print("Level-order Traversal after deletion:", bt.level_order_traversal())

