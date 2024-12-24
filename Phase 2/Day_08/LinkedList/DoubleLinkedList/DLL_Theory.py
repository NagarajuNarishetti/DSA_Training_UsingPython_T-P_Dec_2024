"""
Doubly Linked List (DLL) - Complete Theory and Implementation in Python

A doubly linked list is a linear data structure where each node contains:
1. Data: The actual data of the node.
2. Next: A reference to the next node in the sequence.
3. Prev: A reference to the previous node in the sequence.

Key operations in a doubly linked list:
1. Traversal: Visiting nodes in forward or backward order.
2. Insertion: Adding a new node to the list.
   a. At the beginning
   b. At the end
   c. At a specific position
3. Deletion: Removing a node from the list.
4. Reversal: Reversing the order of the list.
"""

class Node:
    """Class to represent a node in the doubly linked list."""
    def __init__(self, data):
        self.data = data  # Data stored in the node
        self.next = None  # Pointer to the next node
        self.prev = None  # Pointer to the previous node


class DoublyLinkedList:
    """Class to represent a doubly linked list."""
    def __init__(self):
        self.head = None  # Initialize the head of the list as None

    def is_empty(self):
        """Check if the doubly linked list is empty."""
        return self.head is None

    def append(self, data):
        """
        Add a new node at the end of the doubly linked list.
        Time Complexity: O(n)
        """
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node  # If the list is empty, set the new node as head
        else:
            current = self.head
            while current.next:  # Traverse to the last node
                current = current.next
            current.next = new_node  # Link the last node to the new node
            new_node.prev = current  # Link the new node to the last node

    def prepend(self, data):
        """
        Add a new node at the beginning of the doubly linked list.
        Time Complexity: O(1)
        """
        new_node = Node(data)
        if not self.is_empty():
            new_node.next = self.head  # Link the new node to the current head
            self.head.prev = new_node  # Link the current head to the new node
        self.head = new_node  # Update head to the new node

    def insert_after(self, target_data, data):
        """
        Insert a new node after a specific node in the doubly linked list.
        Time Complexity: O(n)
        """
        current = self.head
        while current and current.data != target_data:  # Find the target node
            current = current.next
        if current is None:
            print(f"Node with data {target_data} not found.")
        else:
            new_node = Node(data)
            new_node.next = current.next  # Link the new node to the next node
            new_node.prev = current  # Link the new node to the current node
            if current.next:  # If the current node is not the last node
                current.next.prev = new_node
            current.next = new_node

    def delete(self, data):
        """
        Delete the first node with the given data.
        Time Complexity: O(n)
        """
        if self.is_empty():
            print("The list is empty. Nothing to delete.")
            return

        current = self.head

        # If the node to be deleted is the head
        if current.data == data:
            if current.next:  # If there is a next node
                current.next.prev = None
            self.head = current.next
            return

        # Search for the node to be deleted
        while current and current.data != data:
            current = current.next

        if current is None:
            print(f"Node with data {data} not found.")
        else:
            if current.next:  # If it's not the last node
                current.next.prev = current.prev
            if current.prev:  # If it's not the first node
                current.prev.next = current.next

    def reverse(self):
        """
        Reverse the doubly linked list.
        Time Complexity: O(n)
        """
        current = self.head
        temp = None
        while current:
            # Swap next and prev for the current node
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev  # Move to the next node (which is previous now)
        if temp:  # Set the head to the last node
            self.head = temp.prev

    def display_forward(self):
        """
        Display the linked list in forward order.
        Time Complexity: O(n)
        """
        if self.is_empty():
            return "The doubly linked list is empty."
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def display_backward(self):
        """
        Display the linked list in backward order.
        Time Complexity: O(n)
        """
        if self.is_empty():
            return "The doubly linked list is empty."
        result = []
        current = self.head
        while current.next:  # Traverse to the last node
            current = current.next
        while current:  # Traverse backward
            result.append(current.data)
            current = current.prev
        return result


# Demonstrating the Doubly Linked List
if __name__ == "__main__":
    # Create an empty doubly linked list
    dll = DoublyLinkedList()

    # Append elements to the list
    dll.append(10)
    dll.append(20)
    dll.append(30)
    print("List after appending 10, 20, 30 (forward):", dll.display_forward())
    print("List after appending 10, 20, 30 (backward):", dll.display_backward())

    # Prepend an element to the list
    dll.prepend(5)
    print("List after prepending 5 (forward):", dll.display_forward())

    # Insert an element after a specific node
    dll.insert_after(20, 25)
    print("List after inserting 25 after 20 (forward):", dll.display_forward())

    # Delete an element from the list
    dll.delete(10)
    print("List after deleting 10 (forward):", dll.display_forward())

    # Reverse the doubly linked list
    dll.reverse()
    print("List after reversing (forward):", dll.display_forward())
    print("List after reversing (backward):", dll.display_backward())
