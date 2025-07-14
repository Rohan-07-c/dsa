# Node for circular singly linked list
class CNode:
    def __init__(self, data):
        self.data = data
        self.next = None

# Circular Singly Linked List class
class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = CNode(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head  # Point to itself
            return
        curr = self.head
        while curr.next != self.head:
            curr = curr.next
        curr.next = new_node         # Add new node at the end
        new_node.next = self.head    # Make it circular

    def display(self):
        if not self.head:
            print("Empty List")
            return
        curr = self.head
        while True:
            print(curr.data, end=" → ")
            curr = curr.next
            if curr == self.head:
                break
        print("(Back to Head)")

csll = CircularSinglyLinkedList()

# Insert elements
csll.insert(1)
csll.insert(2)
csll.insert(3)
csll.insert(4)

# Display list
print("Circular Singly Linked List:")
csll.display()
