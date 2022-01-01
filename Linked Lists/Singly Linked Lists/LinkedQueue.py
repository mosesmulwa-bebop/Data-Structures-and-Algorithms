from Node import _Node as Node
from Empty import Empty


class LinkedQueue:
    """FIFO queue implementation using a singly linked list for storage."""

    def __init__(self):
        """Create empty Queue"""

        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        """Return number of queue elements"""
        return self._size

    def is_empty(self):
        """Return True if queue is empty"""
        return self._size == 0

    def first(self):
        """Return the first element in the queue"""
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head.element

    def enqueue(self, e):
        """Add element to back of queue"""
        new_node = Node(e, None)
        if self.is_empty():
            self._head = new_node           # special case, previously empty
        else:
            self._tail.next_node = new_node
        self._tail = new_node
        self._size += 1

    def dequeue(self):
        """Return and remove the element at the front of queue"""
        if self.is_empty():
            raise Empty('Stack is empty')
        answer = self._head.element
        self._head = self._head.next_node
        self._size -= 1
        if self.is_empty():
            self._tail = None               # special case, now empty
        return answer
