class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def extract_min(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        # Replace root with last element and heapify down
        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return min_val

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._heapify_up(parent)

    def _heapify_down(self, index):
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

    def build_heap(self, array):
        self.heap = array[:]
        n = len(self.heap)
        for i in reversed(range(n // 2)):
            self._heapify_down(i)

    def heap_sort(self):
        sorted_list = []
        while self.heap:
            sorted_list.append(self.extract_min())
        return sorted_list

    def display(self):
        print("Heap array:", self.heap)

# ---------------------
# Example Usage & Test
# ---------------------
if __name__ == "__main__":
    arr = [4, 30, 3, 25, 16, 9]

    print("Input array:", arr)

    heap = MinHeap()
    heap.build_heap(arr)
    heap.display()

    print("Extracted Min:", heap.extract_min())
    heap.display()

    print("Inserting 2")
    heap.insert(2)
    heap.display()

    # Heap Sort (Ascending Order)
    heap.build_heap(arr)  # rebuild before sort to keep original intact
    sorted_result = heap.heap_sort()
    print("Heap Sort result:", sorted_result)
