class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Insert a node in sorted order
    def insert_sorted(self, value):
        new_node = Node(value)
        if self.head is None or value < self.head.data:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        while current.next and current.next.data < value:
            current = current.next

        new_node.next = current.next
        current.next = new_node
        
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    # update
    def update(self, old_value, new_value):
        current = self.head
        while current:
            if current.data == old_value:
                current.data = new_value
                print(f"✅ Updated {old_value} to {new_value}")
                return
            current = current.next
        print(f"❌ Value {old_value} not found in the list.")
    # Delete a node with a given value
    def delete(self, value):
        if self.head is None:
            print("List is empty.")
            return

        if self.head.data == value:
            self.head = self.head.next
            return

        current = self.head
        while current.next and current.next.data != value:
            current = current.next

        if current.next is None:
            print(f"Value {value} not found in the list.")
            return

        current.next = current.next.next

    # Search for a value in the list
    def search(self, value):
        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next
        return False

    # Reverse the linked list
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next  # save next node
            current.next = prev       # reverse the link
            prev = current            # move prev forward
            current = next_node       # move current forward
        self.head = prev  # new head is the last node we visited

    # Display the list
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" → ")
            current = current.next
        print("None")
        
        
    def traverse(self):
        """Traverse the list and return all data as a list."""
        elements = []
        curr = self.head
        while curr:
            elements.append(curr.data)
            curr = curr.next
        return elements
        

# ================== Let's Test This ==================

if __name__ == "__main__":
    ll = LinkedList()

    # Insert elements
    for value in [3, 1, 5, 2, 4]:
        ll.insert_sorted(value)
    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_beginning(5)
    ll.insert_at_end(30)

    print(" Sorted Linked List:")
    ll.display()

    print("\nSearching for 3:", ll.search(3))
    print(" Searching for 10:", ll.search(10))
    
    ll.update(3,59)
    ll.display()

    print("\nDeleting 3")
    ll.delete(3)
    ll.display()

    print("\nReversing the list:")
    ll.reverse()
    ll.display()
    
    
# Traverse the list and show contents as list
print("\nTraversed list data:", ll.traverse())  # New usage
