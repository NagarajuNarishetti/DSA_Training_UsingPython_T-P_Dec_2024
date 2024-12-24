"""
Circular Linked List (CLL) - Complete Theory and Implementation in Python

A circular linked list is a linear data structure where:
1. Each node contains data and a pointer to the next node.
2. The last node's pointer points back to the first node, forming a circle.

Key operations in a circular linked list:
1. Traversal: Visiting all nodes in a circular manner.
2. Insertion: Adding a new node to the list.
   a. At the beginning
   b. At the end
   c. After a specific node
3. Deletion: Removing a node from the list.
"""

class Node:
    """Class to represent a node in the circular linked list."""
    def __init__(self, data):
        self.data = data  # Data stored in the node
        self.next = None  # Pointer to the next node


class CircularLinkedList:
    """Class to represent a circular linked list."""
    def __init__(self):
        self.head = None  # Initialize the head of the list as None

    def is_empty(self):
        """Check if the circular linked list is empty."""
        return self.head is None

    def append(self, data):
        """
        Add a new node at the end of the circular linked list.
        Time Complexity: O(n)
        """
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            new_node.next = self.head  # Point to itself, forming a circle
        else:
            current = self.head
            while current.next != self.head:  # Traverse to the last node
                current = current.next
            current.next = new_node  # Link the last node to the new node
            new_node.next = self.head  # Link the new node to the head

    def prepend(self, data):
        """
        Add a new node at the beginning of the circular linked list.
        Time Complexity: O(n)
        """
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            new_node.next = self.head  # Point to itself, forming a circle
        else:
            current = self.head
            while current.next != self.head:  # Traverse to the last node
                current = current.next
            current.next = new_node  # Link the last node to the new node
            new_node.next = self.head  # Link the new node to the head
            self.head = new_node  # Update head to the new node

    def insert_after(self, target_data, data):
        """
        Insert a new node after a specific node in the circular linked list.
        Time Complexity: O(n)
        """
        if self.is_empty():
            print("The list is empty. Cannot insert.")
            return

        current = self.head
        while True:
            if current.data == target_data:  # Target node found
                new_node = Node(data)
                new_node.next = current.next  # Link the new node to the next node
                current.next = new_node  # Link the current node to the new node
                return
            current = current.next
            if current == self.head:  # If we have traversed the entire list
                break

        print(f"Node with data {target_data} not found.")

    def delete(self, data):
        """
        Delete the first node with the given data.
        Time Complexity: O(n)
        """
        if self.is_empty():
            print("The list is empty. Nothing to delete.")
            return

        current = self.head
        prev = None

        # If the node to be deleted is the head
        if current.data == data:
            if current.next == self.head:  # Only one node in the list
                self.head = None
                return
            else:
                while current.next != self.head:  # Traverse to the last node
                    current = current.next
                current.next = self.head.next  # Link last node to the second node
                self.head = self.head.next  # Update head to the second node
                return

        # Search for the node to be deleted
        while current.next != self.head:
            prev = current
            current = current.next
            if current.data == data:
                prev.next = current.next  # Unlink the node
                return

        # If the node to be deleted is the last node
        if current.data == data:
            prev.next = self.head  # Link the second last node to the head

    def display(self):
        """
        Display the circular linked list.
        Time Complexity: O(n)
        """
        if self.is_empty():
            return "The circular linked list is empty."
        result = []
        current = self.head
        while True:
            result.append(current.data)
            current = current.next
            if current == self.head:  # Stop when we reach the head again
                break
        return result


# Demonstrating the Circular Linked List
if __name__ == "__main__":
    # Create an empty circular linked list
    cll = CircularLinkedList()

    # Append elements to the list
    cll.append(10)
    cll.append(20)
    cll.append(30)
    print("List after appending 10, 20, 30:", cll.display())

    # Prepend an element to the list
    cll.prepend(5)
    print("List after prepending 5:", cll.display())

    # Insert an element after a specific node
    cll.insert_after(20, 25)
    print("List after inserting 25 after 20:", cll.display())

    # Delete an element from the list
    cll.delete(10)
    print("List after deleting 10:", cll.display())

    # Delete the last node
    cll.delete(30)
    print("List after deleting 30:", cll.display())
