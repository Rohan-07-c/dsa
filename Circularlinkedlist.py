class CNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_sorted(self, value):
        new_node = CNode(value)
        if not self.head:
            new_node.next = new_node
            self.head = new_node
            return

        if value < self.head.data:
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            curr.next = new_node
            new_node.next = self.head
            self.head = new_node
            return

        curr = self.head
        while (curr.next != self.head) and (curr.next.data < value):
            curr = curr.next
        new_node.next = curr.next
        curr.next = new_node

    def insert_at_beginning(self, data):
        self.insert_sorted(data)

    def insert_at_end(self, data):
        self.insert_sorted(data)
        


    def update(self, old_value, new_value):
        curr = self.head
        if not curr:
            return
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
        prev = None
        while True:
            if curr.data == value:
                if curr == self.head:
                    if curr.next == self.head:
                        self.head = None
                    else:
                        temp = self.head
                        while temp.next != self.head:
                            temp = temp.next
                        temp.next = self.head.next
                        self.head = self.head.next
                else:
                    prev.next = curr.next
                return
            prev = curr
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
        if not self.head or self.head.next == self.head:
            return
        prev = None
        current = self.head
        next_node = None
        first = self.head
        while True:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            if current == self.head:
                break
        self.head.next = prev
        self.head = prev

    def display(self):
        if not self.head:
            print("List is empty")
            return
        curr = self.head
        while True:
            print(curr.data, end=" → ")
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
    cll = CircularLinkedList()

    for val in [3, 6, 1, 4]:
        cll.insert_sorted(val)

    cll.insert_at_beginning(0)
    cll.insert_at_end(10)

    print("🔗 Circular Singly Linked List:")
    cll.display()

    print("🔍 Search 6:", cll.search(6))
    print("🔍 Search 99:", cll.search(99))

    cll.update(3, 33)
    cll.display()

    print("❌ Deleting 1")
    cll.delete(1)
    cll.display()

    print("🔄 Reversing List")
    cll.reverse()
    cll.display()

    print("🧾 Traversed:", cll.traverse())