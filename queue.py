# Implements a queue

class Queue:

    def __init__(self):
        self._data = []
    
    # add element to back of queue
    def enqueue(self, element):
        self._data.append(element)

    # remove and return element from front of queue
    def dequeue(self):
        assert self.size() > 0
        return self._data.pop(0)

    # returns number of elements waiting in the queue
    def size(self):
        return len(self._data)

    # returns frontmost element
    def peek(self):
        return self._data[0]

    # clears the queue
    def empty(self):
        self._data.clear()


q = Queue()          # create new queue
q.enqueue(3)         # add number 3 to back of queue
q.enqueue(1)         # add number 1 to back of queue
q.enqueue(4)         # add number 4 to back of queue
q.enqueue(5)         # add number 5 to back of queue
print(q.peek())      # prints the frontmost element
q.dequeue()          # dequeues one element
print(q.peek())      # prints the frontmost element



