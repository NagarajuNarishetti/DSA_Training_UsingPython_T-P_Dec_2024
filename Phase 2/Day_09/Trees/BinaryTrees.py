"""
All About Binary Trees:
1. Full Binary Tree
2. Complete Binary Tree
3. Perfect Binary Tree
4. Balanced Binary Tree
"""

# Binary Tree Node Structure
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Helper Function to Print Tree in Preorder
def print_tree_preorder(node):
    if node is None:
        return
    print(node.value, end=" ")
    print_tree_preorder(node.left)
    print_tree_preorder(node.right)

# 1. Full Binary Tree
def create_full_binary_tree():
    """
    A Full Binary Tree Example:
            1
           / \
          2   3
         / \
        4   5
    """
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    return root

print("\n1. Full Binary Tree:")
full_tree = create_full_binary_tree()
print("Tree Structure: Each node has 0 or 2 children.")
print("Preorder Traversal:", end=" ")
print_tree_preorder(full_tree)
print("\nCharacteristics: All nodes have 0 or 2 children.")

# 2. Complete Binary Tree
def create_complete_binary_tree():
    """
    A Complete Binary Tree Example:
            1
           / \
          2   3
         / \  /
        4   5 6
    """
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    return root

print("\n2. Complete Binary Tree:")
complete_tree = create_complete_binary_tree()
print("Tree Structure: All levels filled except possibly the last, filled left to right.")
print("Preorder Traversal:", end=" ")
print_tree_preorder(complete_tree)
print("\nCharacteristics: All levels filled except the last, filled left to right.")

# 3. Perfect Binary Tree
def create_perfect_binary_tree():
    """
    A Perfect Binary Tree Example:
            1
           / \
          2   3
         / \ / \
        4  5 6  7
    """
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    return root

print("\n3. Perfect Binary Tree:")
perfect_tree = create_perfect_binary_tree()
print("Tree Structure: All internal nodes have 2 children, and all leaf nodes are at the same level.")
print("Preorder Traversal:", end=" ")
print_tree_preorder(perfect_tree)
print("\nCharacteristics: All internal nodes have two children; all leaves are at the same level.")

# 4. Balanced Binary Tree
def is_balanced(node):
    """
    Helper Function to Check if a Binary Tree is Balanced.
    Returns the height if balanced, -1 otherwise.
    """
    if node is None:
        return 0
    left_height = is_balanced(node.left)
    right_height = is_balanced(node.right)
    if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
        return -1
    return max(left_height, right_height) + 1

def create_balanced_binary_tree():
    """
    A Balanced Binary Tree Example:
            1
           / \
          2   3
         / 
        4
    """
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    return root

print("\n4. Balanced Binary Tree:")
balanced_tree = create_balanced_binary_tree()
print("Tree Structure: The height difference between left and right subtrees is at most 1.")
print("Preorder Traversal:", end=" ")
print_tree_preorder(balanced_tree)
if is_balanced(balanced_tree) != -1:
    print("\nThis is a balanced binary tree.")
else:
    print("\nThis is not a balanced binary tree.")
print("\nCharacteristics: Height difference of left and right subtrees is ≤ 1 for every node.")

# Summary
print("\nSummary of Binary Tree Types:")
print("""
1. Full Binary Tree:
   - Each node has 0 or 2 children.

2. Complete Binary Tree:
   - All levels filled except the last, and nodes in the last level are filled from left to right.

3. Perfect Binary Tree:
   - All internal nodes have 2 children, and all leaf nodes are at the same level.

4. Balanced Binary Tree:
   - The height difference between the left and right subtrees of every node is at most 1.
""")




"""
Binary Tree - Complete Theory and Implementation in Python

A binary tree is a hierarchical data structure where each node has at most two children,
referred to as the left child and the right child.

Key Features of a Binary Tree:
1. Root Node: The topmost node of the tree.
2. Internal Nodes: Nodes that have at least one child.
3. Leaf Nodes: Nodes with no children.
4. Depth: The level of a node in the tree, starting at 0 for the root.
5. Height: Longest path from the root to a leaf node.

Types of Binary Trees:
1. Full Binary Tree: Every node has either 0 or 2 children.
2. Complete Binary Tree: All levels are completely filled except possibly the last level.
3. Perfect Binary Tree: All internal nodes have two children, and all leaf nodes are at the same level.
4. Balanced Binary Tree: Difference in height of left and right subtrees for every node is at most 1.








Common Operations on Binary Trees:
1. Traversals:
   a. In-order (Left -> Root -> Right)
   b. Pre-order (Root -> Left -> Right)
   c. Post-order (Left -> Right -> Root)
   d. Level-order (Breadth-First)
2. Insertion
3. Deletion
4. Search
"""

class Node:
    """
    Class to represent a node in a binary tree.
    Attributes:
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
        Inserts a node into the binary tree using level-order traversal.
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
        Performs in-order traversal (Left -> Root -> Right).
        Time Complexity: O(n)
        """
        if node:
            self.in_order_traversal(node.left, result)
            result.append(node.data)
            self.in_order_traversal(node.right, result)

    def pre_order_traversal(self, node, result):
        """
        Performs pre-order traversal (Root -> Left -> Right).
        Time Complexity: O(n)
        """
        if node:
            result.append(node.data)
            self.pre_order_traversal(node.left, result)
            self.pre_order_traversal(node.right, result)

    def post_order_traversal(self, node, result):
        """
        Performs post-order traversal (Left -> Right -> Root).
        Time Complexity: O(n)
        """
        if node:
            self.post_order_traversal(node.left, result)
            self.post_order_traversal(node.right, result)
            result.append(node.data)

    def level_order_traversal(self):
        """
        Performs level-order traversal (Breadth-First Search).
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

    def search(self, data):
        """
        Searches for a node with the given value.
        Time Complexity: O(n)
        """
        if not self.root:
            return False

        queue = [self.root]
        while queue:
            temp = queue.pop(0)
            if temp.data == data:
                return True
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
        return False


# Demonstrating Binary Tree Operations
if __name__ == "__main__":
    # Create a binary tree
    bt = BinaryTree()

    # Insert nodes into the binary tree
    bt.insert(1)
    bt.insert(2)
    bt.insert(3)
    bt.insert(4)
    bt.insert(5)
    bt.insert(6)
    bt.insert(7)

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

    # Search for a node
    search_value = 5
    if bt.search(search_value):
        print(f"Node with value {search_value} exists in the tree.")
    else:
        print(f"Node with value {search_value} does not exist in the tree.")
