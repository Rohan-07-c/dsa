class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None  # Previous pointer for doubly linked list
        self.next = None  # Next pointer

class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Head node of the list

    # Insert a node in sorted order (ascending)
    def insert_sorted(self, value):
        new_node = Node(value)

        # Case 1: Empty list or insert at beginning
        if self.head is None or value < self.head.data:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            return

        # Case 2: Insert somewhere after the head
        current = self.head
        while current.next and current.next.data < value:
            current = current.next

        new_node.next = current.next
        new_node.prev = current

        if current.next:
            current.next.prev = new_node
        current.next = new_node

    # Insert at a specific 1-based position
    def insert_at(self, position, value):
        new_node = Node(value)

        if position <= 0:
            print("⚠️ Position must be ≥ 1.")
            return

        # Insert at the head
        if position == 1:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            return

        # Traverse to (position - 1)th node
        current = self.head
        index = 1

        while current and index < position - 1:
            current = current.next
            index += 1

        if current is None:
            print("⚠️ Position out of bounds.")
            return

        # Insert in between nodes
        new_node.next = current.next
        new_node.prev = current

        if current.next:
            current.next.prev = new_node
        current.next = new_node

    # Delete a node by value
    def delete(self, value):
        current = self.head

        while current and current.data != value:
            current = current.next

        if current is None:
            print("⚠️ Value not found.")
            return

        # Update previous node’s next
        if current.prev:
            current.prev.next = current.next
        else:
            # Deleting the head node
            self.head = current.next

        # Update next node’s prev
        if current.next:
            current.next.prev = current.prev

    # Search for a value in the list
    def search(self, value):
        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next
        return False

    # Reverse the doubly linked list
    def reverse(self):
        current = self.head
        temp = None

        while current:
            temp = current.prev  # Save the previous
            current.prev = current.next  # Swap prev and next
            current.next = temp
            current = current.prev  # Move to next node (originally prev)

        # Reset head to the new front
        if temp:
            self.head = temp.prev


    # Print the list in readable format
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ⇄ ")
            current = current.next
        print("None")

# =================== DRIVER CODE ===================

if __name__ == "__main__":
    dll = DoublyLinkedList()

    print("🧩 Inserting values in sorted order...")
    for val in [3, 1, 5, 2, 4]:
        dll.insert_sorted(val)
    dll.display()

    print("\n🎯 Inserting at position 3: value 99")
    dll.insert_at(3, 99)
    dll.display()
 
    print("\n🔍 Searching for 5:", dll.search(5))
    print("🔍 Searching for 42:", dll.search(42))

    print("\n🧼 Deleting value 3")
    dll.delete(3)
    dll.display()

    print("\n🔄 Reversing the list")
    dll.reverse()
    dll.display()
