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

# ================== Let's Test This ==================

if __name__ == "__main__":
    ll = LinkedList()

    # Insert elements
    for value in [3, 1, 5, 2, 4]:
        ll.insert_sorted(value)

    print("🔗 Sorted Linked List:")
    ll.display()

    print("\n🔍 Searching for 3:", ll.search(3))
    print("🔍 Searching for 10:", ll.search(10))
    
    ll.update(3,59)
    ll.display()

    print("\n❌ Deleting 3")
    ll.delete(3)
    ll.display()

    print("\n🔄 Reversing the list:")
    ll.reverse()
    ll.display()
