# Node class for singly linked list
class Node:
    def __init__(self, data):
        self.data = data  # Value of the node
        self.next = None  # Pointer to the next node

# Singly Linked List class
class SinglyLinkedList:
    def __init__(self):
        self.head = None  # Head of the list (first node)

    def insert_at_end(self, data):
        # Create a new node
        new_node = Node(data)
        if not self.head:
            # If list is empty, make new_node the head
            self.head = new_node
            return
        # Traverse to the end of the list
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node  # Add new node at the end

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head  # Point new node to the current head
        self.head = new_node       # Update head to the new node

    def delete_by_value(self, value):
        if not self.head:
            return
        if self.head.data == value:
            self.head = self.head.next  # Remove head
            return
        curr = self.head
        while curr.next and curr.next.data != value:
            curr = curr.next
        if curr.next:
            curr.next = curr.next.next  # Bypass the node to delete it

    def display(self):
        curr = self.head
        while curr:
            print(curr.data, end=" → ")
            curr = curr.next
        print("None")

sll = SinglyLinkedList()

# Insert elements
sll.insert_at_end(10)
sll.insert_at_end(20)
sll.insert_at_beginning(5)
sll.insert_at_end(30)

# Display list
print("Singly Linked List:")
sll.display()

# Delete an element
sll.delete_by_value(20)
print("After deleting 20:")
sll.display()
