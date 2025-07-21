class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_sorted(self, value):
        new_node = DNode(value)
        if self.head is None or value < self.head.data:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            return

        curr = self.head
        while curr.next and curr.next.data < value:
            curr = curr.next

        new_node.next = curr.next
        if curr.next:
            curr.next.prev = new_node
        new_node.prev = curr
        curr.next = new_node

    def insert_at_beginning(self, data):
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

    def update(self, old_value, new_value):
        curr = self.head
        while curr:
            if curr.data == old_value:
                curr.data = new_value
                print(f"✅ Updated {old_value} to {new_value}")
                return
            curr = curr.next
        print(f"❌ Value {old_value} not found")

    def delete(self, value):
        curr = self.head
        while curr:
            if curr.data == value:
                if curr.prev:
                    curr.prev.next = curr.next
                else:
                    self.head = curr.next
                if curr.next:
                    curr.next.prev = curr.prev
                return
            curr = curr.next
        print(f"❌ Value {value} not found")

    def search(self, value):
        curr = self.head
        while curr:
            if curr.data == value:
                return True
            curr = curr.next
        return False

    def reverse(self):
        curr = self.head
        temp = None
        while curr:
            temp = curr.prev
            curr.prev = curr.next
            curr.next = temp
            curr = curr.prev
        if temp:
            self.head = temp.prev

    def display(self):
        curr = self.head
        while curr:
            print(curr.data, end=" ⇄ ")
            curr = curr.next
        print("None")

    def traverse(self):
        elements = []
        curr = self.head
        while curr:
            elements.append(curr.data)
            curr = curr.next
        return elements

if __name__ == "__main__":
    dll = DoublyLinkedList()

    for val in [4, 2, 7, 1, 5]:
        dll.insert_sorted(val)

    dll.insert_at_beginning(0)
    dll.insert_at_end(9)

    print("🔗 Doubly Linked List:")
    dll.display()

    print("🔍 Search 5:", dll.search(5))
    print("🔍 Search 99:", dll.search(99))

    dll.update(5, 55)
    dll.display()

    print("❌ Deleting 2")
    dll.delete(2)
    dll.display()

    print("🔄 Reversing List")
    dll.reverse()
    dll.display()

    print("🧾 Traversed:", dll.traverse())