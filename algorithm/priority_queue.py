
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
        if self.is_empty():
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
            if self.elements[index].priority == self.elements[leftchild_index].priority:
                if self.elements[index].order > self.elements[leftchild_index].order:
                    smallest_index = leftchild_index
            else:
                smallest_index = leftchild_index
        if rightchild_index < self.size and self.elements[smallest_index].priority >= self.elements[rightchild_index].priority:
            if self.elements[smallest_index].priority == self.elements[rightchild_index].priority:
                if self.elements[smallest_index].order > self.elements[rightchild_index].order:
                    smallest_index = rightchild_index
            else:
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


# JobRunner class having a priority queue
class JobRunner(MinHeap):
    def __init__(self) -> None:
        super().__init__()
        self.pending_task = None

    def prepare_pending_task(self):
        self.pending_task = self.extractMin()   # change function name to extract_min()

    def run_task(self):
        self.pending_task.run()


# Job class having a message, priority [lower value is assumed a higher priority], and order
class Job:
    def __init__(self, priority, order) -> None:
        self.priority = priority
        self.order = order
        self.message = "A task with priority=" + str(self.priority) + ", order=" + str(self.order)

    def run(self):
        print("Running task...")
        print(self.message)
        print("Task is finished...")


import sys 
def main():
    jobRunner = JobRunner()
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    for i in range(n, 0, -1):
        job = Job(priority=i, order=(n-i+1))
        jobRunner.add(job)
        print([(x.priority, x.order) for x in jobRunner.elements])

    print("JobRunner is filled up with jobs, now time to dequeue and run tasks w.r.t priorities")

    while not jobRunner.is_empty():
        pending_task = jobRunner.extractMin()
        pending_task.run()
        print([(x.priority, x.order) for x in jobRunner.elements])

    print("Done")

if __name__ == "__main__":
    main()