# Node for circular doubly linked list
class CDNode:
    def __init__(self, data):
        self.data = data
        self.next = self  # Point to self initially
        self.prev = self

# Circular Doubly Linked List class
class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = CDNode(data)
        if not self.head:
            self.head = new_node  # First node points to itself
        else:
            tail = self.head.prev       # Get the last node
            new_node.prev = tail
            new_node.next = self.head
            tail.next = new_node        # Tail's next is new node
            self.head.prev = new_node   # Head's prev is new node

    def display_forward(self):
        if not self.head:
            print("Empty List")
            return
        curr = self.head
        while True:
            print(curr.data, end=" ⇄ ")
            curr = curr.next
            if curr == self.head:
                break
        print("(Back to Head)")

    def display_backward(self):
        if not self.head:
            print("Empty List")
            return
        curr = self.head.prev  # Start at the last node
        start = curr
        while True:
            print(curr.data, end=" ⇄ ")
            curr = curr.prev
            if curr == start:
                break
        print("(Back to Tail)")

cdll = CircularDoublyLinkedList()

# Insert elements
cdll.insert(10)
cdll.insert(20)
cdll.insert(30)
cdll.insert(40)

# Display forward and backward
print("Circular Doubly Linked List (forward):")
cdll.display_forward()

print("Circular Doubly Linked List (backward):")
cdll.display_backward()
