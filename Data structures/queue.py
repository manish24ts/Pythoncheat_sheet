class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        # Add item to the end of the queue
        self.queue.append(item)

    def dequeue(self):
        # Remove item from the front of the queue
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return "Queue is empty"

    def peek(self):
        # See the front item without removing it
        if not self.is_empty():
            return self.queue[0]
        else:
            return "Queue is empty"

    def is_empty(self):
        # Check if the queue is empty
        return len(self.queue) == 0

    def size(self):
        # Get the size of the queue
        return len(self.queue)

# Example usage
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print("Front element:", q.peek())  # Output: Front element: 10
print("Removed element:", q.dequeue())  # Output: Removed element: 10
print("Queue size:", q.size())  # Output: Queue size: 2
