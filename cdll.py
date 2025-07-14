class CDNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = CDNode(value)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
            return

        last = self.head.prev
        last.next = new_node
        new_node.prev = last
        new_node.next = self.head
        self.head.prev = new_node

    def delete(self, value):
        if not self.head:
            print("⚠️ CDLL is empty.")
            return

        current = self.head
        while True:
            if current.data == value:
                if current.next == current:  # Only one node
                    self.head = None
                    return
                current.prev.next = current.next
                current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
                return
            current = current.next
            if current == self.head:
                break
        print("❌ Value not found in CDLL.")

    def update(self, old_value, new_value):
        if not self.head:
            print("⚠️ CDLL is empty.")
            return
        current = self.head
        while True:
            if current.data == old_value:
                current.data = new_value
                print(f"🔧 CDLL: Updated {old_value} → {new_value}")
                return
            current = current.next
            if current == self.head:
                break
        print(f"❌ {old_value} not found in CDLL.")

    def display_forward(self):
        if not self.head:
            print("CDLL (forward): None")
            return
        current = self.head
        print("CDLL (forward): ", end="")
        while True:
            print(current.data, end=" ⇄ ")
            current = current.next
            if current == self.head:
                break
        print("(head again 🔁)")

    def display_backward(self):
        if not self.head:
            print("CDLL (backward): None")
            return
        current = self.head.prev
        print("CDLL (backward): ", end="")
        while True:
            print(current.data, end=" ⇄ ")
            current = current.prev
            if current == self.head.prev:
                break
        print("(tail again 🔁)")

# 🔁 Test CDLL
print("\n=== 🔁 Circular Doubly Linked List ===")
cdll = CircularDoublyLinkedList()
for val in [100, 200, 300, 400]:
    cdll.insert(val)
cdll.display_forward()

cdll.update(200, 222)
cdll.display_forward()
cdll.display_backward()

cdll.delete(100)
cdll.display_forward()

cdll.update(999, 111)  # Should show not found
