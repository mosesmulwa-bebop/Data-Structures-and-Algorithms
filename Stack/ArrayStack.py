from Empty import Empty


class ArrayStack:
    """Implementation of a stack in python code using a list
    Methods - Push(e), pop, is_empty, length, top
    """

    def __init__(self):
        self._data = []

    def push(self, e):
        """Add an element to the top of the stack. Append to the list"""
        self._data.append(e)

    def pop(self):
        """Remove and return the element on top of the stack
        Raise exception if stack is empty
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        cur = self.top()
        self._data.pop()
        return cur

    def top(self):
        """Return the element on top of stack. End of list"""
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]

    def is_empty(self):
        """Boolean on whether stack is empty or not"""
        return len(self) == 0

    def __len__(self):
        """Return length of the stack. Here return length of the list"""
        return len(self._data)





