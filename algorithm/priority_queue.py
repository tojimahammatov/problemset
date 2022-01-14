
# priority queue implementation
# heaps are used

class MinHeap:
    def __init__(self) -> None:
        self.elements = []
        self.size = 0

    def add(self, item):
        self.elements.append(item)
        self.size += 1
        self.min_heapify_bottom2top(self.size - 1)

    def extractMin(self):
        if len(self.elements) == 0:
            raise Exception("heap is empty")
        min_element = self.elements[0]
        last_element = self.elements.pop()
        self.size -= 1
        if self.size > 0:
            self.elements[0] = last_element
            self.min_heapify_top2bottom(0)
        return min_element

    def min_heapify_top2bottom(self, index):
        leftchild_index = 2 * index + 1
        rightchild_index = 2 * index + 2
        smallest_index = index
        if leftchild_index < self.size and self.elements[index].priority >= self.elements[leftchild_index].priority:
            smallest_index = leftchild_index
        if rightchild_index < self.size and self.elements[smallest_index].priority >= self.elements[rightchild_index].priority:
            smallest_index = rightchild_index
        if index != smallest_index:
            self.elements[index], self.elements[smallest_index] = self.elements[smallest_index], self.elements[index]
            self.min_heapify_top2bottom(smallest_index)

    def min_heapify_bottom2top(self, index):
        parent_index = (index - 1) // 2
        if parent_index >= 0 and self.elements[parent_index].priority > self.elements[index].priority:
            self.elements[index], self.elements[parent_index] = self.elements[parent_index], self.elements[index]
            self.min_heapify_bottom2top(parent_index)

    def is_empty(self):
        return len(self.elements) == 0


class Job:
    def __init__(self, priority, order, message) -> None:
        self.priority = priority
        self.order = order
        self.message = message

    def run(self):
        print("Running task...")
        print(self.message)
        print("Task is finished...")