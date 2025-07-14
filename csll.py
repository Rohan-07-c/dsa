class CSNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = CSNode(value)
        if not self.head:
            self.head = new_node
            new_node.next = self.head  # Loop to self
            return
        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = new_node
        new_node.next = self.head  # Point last to head again

    def delete(self, value):
        if not self.head:
            print("⚠️ CSLL is empty.")
            return

        current = self.head
        prev = None

        while True:
            if current.data == value:
                if current == self.head:
                    if current.next == self.head:
                        self.head = None
                        return
                    # Find last node
                    last = self.head
                    while last.next != self.head:
                        last = last.next
                    self.head = current.next
                    last.next = self.head
                    return
                else:
                    prev.next = current.next
                    return

            prev = current
            current = current.next
            if current == self.head:
                break
        print("❌ Value not found in CSLL.")

    def update(self, old_value, new_value):
        if not self.head:
            print("⚠️ CSLL is empty.")
            return
        current = self.head
        while True:
            if current.data == old_value:
                current.data = new_value
                print(f"🔧 CSLL: Updated {old_value} → {new_value}")
                return
            current = current.next
            if current == self.head:
                break
        print(f"❌ {old_value} not found in CSLL.")

    def display(self):
        if not self.head:
            print("CSLL: None (empty circle)")
            return
        current = self.head
        print("CSLL: ", end="")
        while True:
            print(current.data, end=" → ")
            current = current.next
            if current == self.head:
                break
        print("(back to head 🔁)")

# 🔁 Test CSLL
print("=== 🔁 Circular Singly Linked List ===")
csll = CircularSinglyLinkedList()
for val in [10, 20, 30, 40]:
    csll.insert(val)
csll.display()

csll.update(30, 300)
csll.display()

csll.delete(10)
csll.display()

csll.update(100, 999)  # Should show not found
