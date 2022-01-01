from Empty import Empty


class ArrayDeque:
    """Implementation of the double ended queue using list as underlying storage"""
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * ArrayDeque.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def first(self):
        """Return but don't remove the first element"""
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._data[self._front]

    def last(self):
        """Return but don't remove the first element"""
        if self.is_empty():
            raise Empty('Deque is empty')
        last = (self._front + self._size - 1) % len(self._data)
        return self._data[last]

    def is_empty(self):
        """Return true if queue has no elements"""
        return self._size == 0

    def _resize(self, cap):
        """Internal utility to resize underlying array"""
        old = self._data
        self._data = [None] * cap

        index_of_first = self._front
        for k in range(self._size):
            self._data[k] = old[index_of_first]
            index_of_first = (index_of_first + 1) % len(old)

        self._front = 0                                                     # front has been reset

    def add_first(self, e):
        """Add element to the front of queue"""
        if self._size == len(self._data):                                    # check if there is space
            self._resize(len(self._data) * 2)                                # double the capacity

        if self._data[self._front] is not None:
            self._front = (self._front - 1) % len(self._data)
        self._data[self._front] = e
        self._size += 1

    def delete_first(self):
        """Remove and return element at the front of the queue"""
        if self.is_empty():
            raise Empty('Deque is empty')
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        if self._size < (len(self._data) // 4):  # if no of elements is less than a quarter of current length of array
            self._resize(len(self._data) // 2)  # resize to half current size
        return answer

    def add_last(self, e):
        """Add element e to the back of the queue"""
        if self._size == len(self._data):                                    # check if there is space
            self._resize(len(self._data) * 2)                                # double the capacity
        last_index = (self._front + self._size) % len(self._data)
        self._data[last_index] = e
        self._size += 1

    def delete_last(self):
        """Delete element at the back of the queue"""
        last_index = (self._front + self._size - 1) % len(self._data)
        answer = self._data[last_index]
        self._data[last_index] = None
        self._size -= 1
        if self._size < (len(self._data) // 4):   # if no of elements is less than a quarter of current length of array
            self._resize(len(self._data) // 2)    # resize to half current size
        return answer

    def __len__(self):
        """Return number of elements in deque"""
        return self._size

    def __str__(self):
        """Return string version of current queue"""
        return ''.join(str(self._data))
