import random

# Node in a skip list
class SkipNode:
    def __init__(self, data, level):
        self.data = data
        self.forward = [None]*level  # Multiple levels (like layers in a cake)

class SkipList:
    MAX_LEVEL = 4  # Adjust based on use case

    def __init__(self):
        self.head = SkipNode(-1, self.MAX_LEVEL)  # Sentinel node

    def random_level(self):
        level = 1
        while random.random() < 0.5 and level < self.MAX_LEVEL:
            level += 1
        return level

    def insert(self, data):
        update = [None]*self.MAX_LEVEL
        curr = self.head

        # Find the position to insert
        for i in reversed(range(self.MAX_LEVEL)):
            while curr.forward[i] and curr.forward[i].data < data:
                curr = curr.forward[i]
            update[i] = curr

        level = self.random_level()
        new_node = SkipNode(data, level)

        # Rewire the forward pointers
        for i in range(level):
            new_node.forward[i] = update[i].forward[i]
            update[i].forward[i] = new_node

    def display(self):
        print("Skip List:")
        for i in range(self.MAX_LEVEL):
            curr = self.head.forward[i]
            print(f"Level {i+1}: ", end="")
            while curr:
                print(curr.data, end=" → ")
                curr = curr.forward[i]
            print("None")

slist = SkipList()

# Insert elements
slist.insert(3)
slist.insert(6)
slist.insert(7)
slist.insert(9)
slist.insert(12)
slist.insert(19)

# Display list levels
slist.display()
