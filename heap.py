class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        # Add value to end and heapify up
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def delete_max(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        # Swap max with last and heapify down
        max_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return max_val

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[index] > self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._heapify_up(parent)

    def _heapify_down(self, index):
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2

        # Find largest among index, left and right
        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right

        # If largest is not index, swap and recurse
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)

    def is_heap(self):
        # Check for heap condition: each parent ≥ children
        n = len(self.heap)
        for i in range(n):
            left = 2 * i + 1
            right = 2 * i + 2

            if left < n and self.heap[i] < self.heap[left]:
                return False
            if right < n and self.heap[i] < self.heap[right]:
                return False
        return True

    def display(self):
        print("Heap array:", self.heap)


# ---------------------
# Example usage
# ---------------------
if __name__ == "__main__":
    h = MaxHeap()

    # Insert values
    for val in [20, 15, 30, 40, 10, 5, 60]:
        h.insert(val)
    h.display()

    # Check heap condition
    print("Heap condition satisfied?", h.is_heap())

    # Delete max value
    print("Deleted max:", h.delete_max())
    h.display()
    print("Heap condition satisfied?", h.is_heap())
