# class Node:
#     def __init__(self,data=None,next=None):
#         self.data=data
#         self.next=next
    
#     def addAtFirst(data):
#         temp=Node()

"""
Single Linked List (SLL) - Complete Theory and Implementation in Python

A single linked list is a linear data structure consisting of nodes, where each node contains:
1. Data: The actual data of the node.
2. Next: A reference (or pointer) to the next node in the sequence.

Key operations in a single linked list:
1. Traversal: Visiting each node to access data.
2. Insertion: Adding a new node to the list.
   a. At the beginning
   b. At the end
   c. At a specific position
3. Deletion: Removing a node from the list.
4. Reversal: Reversing the order of the list.
"""

class Node:
    """Class to represent a node in the linked list."""
    def __init__(self, data):
        self.data = data  # Data stored in the node
        self.next = None  # Pointer to the next node (initially None)


class SingleLinkedList:
    """Class to represent a single linked list."""
    def __init__(self):
        self.head = None  # Initialize the head of the list as None

    def is_empty(self):
        """Check if the linked list is empty."""
        return self.head is None

    def append(self, data):
        """
        Add a new node at the end of the linked list.
        Time Complexity: O(n)
        """
        new_node = Node(data)
        if self.is_empty():  # If the list is empty, set the new node as head
            self.head = new_node
        else:
            current = self.head
            while current.next:  # Traverse to the last node
                current = current.next
            current.next = new_node  # Link the last node to the new node

    def prepend(self, data):
        """
        Add a new node at the beginning of the linked list.
        Time Complexity: O(1)
        """
        new_node = Node(data)
        new_node.next = self.head  # Link the new node to the current head
        self.head = new_node  # Update head to the new node

    def insert_after(self, target_data, data):
        """
        Insert a new node after a specific node in the list.
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
            current.next = new_node  # Link the target node to the new node

    def delete(self, data):
        """
        Delete the first node with the given data.
        Time Complexity: O(n)
        """
        if self.is_empty():
            print("The list is empty. Nothing to delete.")
            return

        # If the node to be deleted is the head
        if self.head.data == data:
            self.head = self.head.next  # Update head to the next node
            return

        # Search for the node to be deleted
        current = self.head
        while current.next and current.next.data != data:
            current = current.next

        if current.next is None:
            print(f"Node with data {data} not found.")
        else:
            current.next = current.next.next  # Remove the node by skipping it

    def reverse(self):
        """
        Reverse the linked list.
        Time Complexity: O(n)
        """
        prev = None
        current = self.head
        while current:
            next_node = current.next  # Store the next node
            current.next = prev  # Reverse the link
            prev = current  # Move prev to the current node
            current = next_node  # Move current to the next node
        self.head = prev  # Update head to the new front of the list

    def display(self):
        """
        Display the linked list as a list of data.
        Time Complexity: O(n)
        """
        if self.is_empty():
            return "The linked list is empty."
        result = []
        current = self.head
        while current:
            result.append(current.data)  # Collect the data
            current = current.next
        return result


# Demonstrating the Single Linked List
if __name__ == "__main__":
    # Create an empty linked list
    sll = SingleLinkedList()

    # Append elements to the list
    sll.append(10)
    sll.append(20)
    sll.append(30)
    print("List after appending 10, 20, 30:", sll.display())

    # Prepend an element to the list
    sll.prepend(5)
    print("List after prepending 5:", sll.display())

    # Insert an element after a specific node
    sll.insert_after(20, 25)
    print("List after inserting 25 after 20:", sll.display())

    # Delete an element from the list
    sll.delete(10)
    print("List after deleting 10:", sll.display())

    # Reverse the linked list
    sll.reverse()
    print("List after reversing:", sll.display())

        