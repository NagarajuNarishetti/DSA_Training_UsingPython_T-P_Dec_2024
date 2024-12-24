# Queue Implementation in Python

# A queue is a linear data structure that follows the First In, First Out (FIFO) principle.
# In a queue, the element that is added first is the one that is removed first.
# It has two primary operations:
# 1. enqueue: to add an element to the end of the queue
# 2. dequeue: to remove an element from the front of the queue

# Queue can be implemented using various ways:
# 1. Using lists
# 2. Using collections.deque
# 3. Using a custom Node-based structure

# Let's go through these implementations step-by-step.

# 1. Implementing Queue using List
class QueueUsingList:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        """Adds an item to the end of the queue"""
        self.queue.append(item)
        print(f'Enqueued: {item}')
    
    def dequeue(self):
        """Removes and returns the item from the front of the queue"""
        if len(self.queue) > 0:
            removed_item = self.queue.pop(0)
            print(f'Dequeued: {removed_item}')
            return removed_item
        else:
            print("Queue is empty!")
            return None
    
    def peek(self):
        """Returns the item at the front without removing it"""
        if len(self.queue) > 0:
            return self.queue[0]
        else:
            print("Queue is empty!")
            return None
    
    def is_empty(self):
        """Returns True if the queue is empty, False otherwise"""
        return len(self.queue) == 0
    
    def size(self):
        """Returns the number of items in the queue"""
        return len(self.queue)

# 2. Implementing Queue using collections.deque
from collections import deque

class QueueUsingDeque:
    def __init__(self):
        self.queue = deque()
    
    def enqueue(self, item):
        """Adds an item to the end of the queue"""
        self.queue.append(item)
        print(f'Enqueued: {item}')
    
    def dequeue(self):
        """Removes and returns the item from the front of the queue"""
        if len(self.queue) > 0:
            removed_item = self.queue.popleft()
            print(f'Dequeued: {removed_item}')
            return removed_item
        else:
            print("Queue is empty!")
            return None
    
    def peek(self):
        """Returns the item at the front without removing it"""
        if len(self.queue) > 0:
            return self.queue[0]
        else:
            print("Queue is empty!")
            return None
    
    def is_empty(self):
        """Returns True if the queue is empty, False otherwise"""
        return len(self.queue) == 0
    
    def size(self):
        """Returns the number of items in the queue"""
        return len(self.queue)

# 3. Implementing Queue using Node-based Structure (Linked List)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class QueueUsingNodes:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def enqueue(self, item):
        """Adds an item to the end of the queue"""
        new_node = Node(item)
        if self.rear is None:
            self.front = self.rear = new_node
            print(f'Enqueued: {item}')
            return
        self.rear.next = new_node
        self.rear = new_node
        print(f'Enqueued: {item}')
    
    def dequeue(self):
        """Removes and returns the item from the front of the queue"""
        if self.front is None:
            print("Queue is empty!")
            return None
        removed_item = self.front.data
        self.front = self.front.next
        if self.front is None:  # If the queue is empty now
            self.rear = None
        print(f'Dequeued: {removed_item}')
        return removed_item
    
    def peek(self):
        """Returns the item at the front without removing it"""
        if self.front is not None:
            return self.front.data
        else:
            print("Queue is empty!")
            return None
    
    def is_empty(self):
        """Returns True if the queue is empty, False otherwise"""
        return self.front is None
    
    def size(self):
        """Returns the number of items in the queue"""
        current = self.front
        count = 0
        while current:
            count += 1
            current = current.next
        return count

# Demonstrating all implementations:

# Using Queue with List
print("Queue using List:")
q_list = QueueUsingList()
q_list.enqueue(10)
q_list.enqueue(20)
q_list.enqueue(30)
print(f"Front item: {q_list.peek()}")
q_list.dequeue()
print(f"Queue size: {q_list.size()}")
q_list.dequeue()

# Using Queue with Deque
print("\nQueue using Deque:")
q_deque = QueueUsingDeque()
q_deque.enqueue(40)
q_deque.enqueue(50)
print(f"Front item: {q_deque.peek()}")
q_deque.dequeue()
print(f"Queue size: {q_deque.size()}")

# Using Queue with Nodes
print("\nQueue using Nodes:")
q_nodes = QueueUsingNodes()
q_nodes.enqueue(60)
q_nodes.enqueue(70)
q_nodes.enqueue(80)
print(f"Front item: {q_nodes.peek()}")
q_nodes.dequeue()
print(f"Queue size: {q_nodes.size()}")
