from Node import _Node as Node
from Empty import Empty


class LinkedStack:
    """Implementation of LIFO Stack ADT using a singly linked list"""

    def __init__(self):
        self._size = 0                          # number of stack elements
        self._head = None                       # reference to head node

    def __len__(self):
        """Return number of stack elements"""
        return self._size

    def is_empty(self):
        """Return True if stack is empty"""
        return self._size == 0

    def push(self, e):
        """Add element e to top of stack(front of singly linked list)"""
        self._head = Node(e, self._head)           # create a link a new node
        self._size += 1

    def pop(self):
        """Remove and return element at top of stack(front of list)"""
        if self.is_empty():
            raise Empty('Stack is empty')
        answer = self._head.element
        self._head = self._head.next_node
        self._size -= 1
        return answer

    def top(self):
        """Return element at the top"""
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head.element


