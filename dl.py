class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_front(self, data):
        new_node = DNode(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    def insert_at_end(self, data):
        new_node = DNode(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        new_node.prev = curr

    def delete_by_value(self, value):
        curr = self.head
        while curr and curr.data != value:
            curr = curr.next
        if not curr:
            return
        if curr.prev:
            curr.prev.next = curr.next
        else:
            self.head = curr.next
        if curr.next:
            curr.next.prev = curr.prev

    def display_forward(self):
        curr = self.head
        while curr:
            print(curr.data, end=" ⇄ ")
            curr = curr.next
        print("None")

    def display_backward(self):
        curr = self.head
        if not curr:
            return
        while curr.next:
            curr = curr.next
        while curr:
            print(curr.data, end=" ⇄ ")
            curr = curr.prev
        print("None")

dll = DoublyLinkedList()

# Insert elements
dll.insert_at_end(100)
dll.insert_at_end(200)
dll.insert_at_front(50)
dll.insert_at_front(25)

# Display list forward and backward
print("Doubly Linked List (forward):")
dll.display_forward()

print("Doubly Linked List (backward):")
dll.display_backward()

# Delete an element
dll.delete_by_value(100)
print("After deleting 100:")
dll.display_forward()
dll.display_backward()
