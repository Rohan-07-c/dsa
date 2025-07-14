# Define the Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Insert a node into the linked list while maintaining sorted order
def insert_sorted(head, value):
    new_node = Node(value)

    # If the list is empty or new value is less than head, insert at beginning
    if head is None or value < head.data:
        new_node.next = head
        return new_node

    # Traverse to the correct position
    current = head
    while current.next and current.next.data < value:
        current = current.next

    # Insert the node
    new_node.next = current.next
    current.next = new_node

    return head

# Traverse and print the linked list
def traverse_linked_list(head):
    while head:
        print(head.data, end=" ")
        head = head.next
    print()

# Main execution logic
if __name__ == "__main__":
    head = None  # Start with an empty list

    # Insert elements (they will be sorted as we insert)
    head = insert_sorted(head, 3)
    head = insert_sorted(head, 1)
    head = insert_sorted(head, 5)
    head = insert_sorted(head, 2)
    head = insert_sorted(head, 4)

    print("Sorted Linked List:")
    traverse_linked_list(head)
