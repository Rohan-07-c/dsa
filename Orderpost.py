# -------- Binary Tree using Linked List --------
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class LinkedBinaryTree:
    def __init__(self):
        self.root = None

    # Build from Inorder and Postorder
    def build_from_in_post(self, inorder, postorder):
        self.post_index = len(postorder) - 1
        in_map = {val: idx for idx, val in enumerate(inorder)}  # value -> index map

        def build(in_start, in_end):
            if in_start > in_end:
                return None
            node_val = postorder[self.post_index]
            self.post_index -= 1
            node = Node(node_val)
            if in_start == in_end:
                return node
            in_index = in_map[node_val]
            # Build right subtree first (important for postorder)
            node.right = build(in_index + 1, in_end)
            node.left = build(in_start, in_index - 1)
            return node

        self.root = build(0, len(inorder) - 1)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=' ')
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.data, end=' ')
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=' ')

    def display_level_order(self, root):
        print("Level Order Traversal:")
        if root is None:
            print("Tree is empty.")
            return
        queue = [root]
        level = 0
        while queue:
            level_size = len(queue)
            print(f"Level {level}:", end=" ")
            for _ in range(level_size):
                current = queue.pop(0)
                print(current.data, end=' ')
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            print()
            level += 1


# -------- Main Program --------
if __name__ == "__main__":
    print("===== Build Binary Tree from Inorder and Postorder =====")
    
    inorder = ['D', 'B', 'E', 'A', 'C']
    postorder = ['D', 'E', 'B', 'C', 'A']

    print("Given Inorder:   ", inorder)
    print("Given Postorder:", postorder)

    lbtree = LinkedBinaryTree()
    lbtree.build_from_in_post(inorder, postorder)

    print("\nLevel Order Display:")
    lbtree.display_level_order(lbtree.root)

    print("Inorder Traversal:   ")
    lbtree.inorder(lbtree.root)

    print("\nPreorder Traversal:  ")
    lbtree.preorder(lbtree.root)

    print("\nPostorder Traversal: ")
    lbtree.postorder(lbtree.root)
