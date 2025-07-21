class CDNode:
    def __init__(self, data):
        self.data = data
        self.prev = self
        self.next = self

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_sorted(self, value):
        new_node = CDNode(value)
        if not self.head:
            self.head = new_node
            return

        curr = self.head
        while curr.next != self.head and curr.next.data < value:
            curr = curr.next

        new_node.next = curr.next
        new_node.prev = curr
        curr.next.prev = new_node
        curr.next = new_node

        if value < self.head.data:
            self.head = new_node

    def insert_at_beginning(self, value):
        self.insert_sorted(value)

    def insert_at_end(self, value):
        self.insert_sorted(value)

    def update(self, old_value, new_value):
        if not self.head:
            return
        curr = self.head
        while True:
            if curr.data == old_value:
                curr.data = new_value
                print(f"✅ Updated {old_value} to {new_value}")
                return
            curr = curr.next
            if curr == self.head:
                break
        print(f"❌ Value {old_value} not found")

    def delete(self, value):
        if not self.head:
            print("List is empty")
            return
        curr = self.head
        while True:
            if curr.data == value:
                if curr == self.head and curr.next == self.head:
                    self.head = None
                else:
                    curr.prev.next = curr.next
                    curr.next.prev = curr.prev
                    if curr == self.head:
                        self.head = curr.next
                return
            curr = curr.next
            if curr == self.head:
                break
        print(f"❌ Value {value} not found")

    def search(self, value):
        curr = self.head
        if not curr:
            return False
        while True:
            if curr.data == value:
                return True
            curr = curr.next
            if curr == self.head:
                break
        return False

    def reverse(self):
        if not self.head:
            return
        curr = self.head
        while True:
            curr.next, curr.prev = curr.prev, curr.next
            curr = curr.prev
            if curr == self.head:
                break
        self.head = self.head.next

    def display(self):
        if not self.head:
            print("List is empty")
            return
        curr = self.head
        while True:
            print(curr.data, end=" ⇄ ")
            curr = curr.next
            if curr == self.head:
                break
        print("(head)")

    def traverse(self):
        elements = []
        if not self.head:
            return elements
        curr = self.head
        while True:
            elements.append(curr.data)
            curr = curr.next
            if curr == self.head:
                break
        return elements


if __name__ == "__main__":
    cdll = CircularDoublyLinkedList()

    for val in [5, 2, 8, 1, 6]:
        cdll.insert_sorted(val)

    cdll.insert_at_beginning(0)
    cdll.insert_at_end(10)

    print("🔗 Circular Doubly Linked List:")
    cdll.display()

    print("🔍 Search 8:", cdll.search(8))
    print("🔍 Search 99:", cdll.search(99))

    cdll.update(6, 66)
    cdll.display()

    print("❌ Deleting 5")
    cdll.delete(5)
    cdll.display()

    print("🔄 Reversing List")
    cdll.reverse()
    cdll.display()

    print("🧾 Traversed:", cdll.traverse())