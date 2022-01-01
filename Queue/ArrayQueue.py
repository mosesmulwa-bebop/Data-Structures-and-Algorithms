from Empty import Empty


class ArrayQueue:
    """Implementation of the Queue ADT using a list as underlying storage"""

    DEFAULT_CAPACITY = 10               # moderate capacity for all new queues

    def __init__(self):
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY                                    # create empty list
        self._index_of_first = 0
        self._size = 0

    def enqueue(self, e):
        """Add element e to the back of queue"""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))  # double the array size

        avail = (self._index_of_first + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def dequeue(self):
        """Remove and return the first element from queue Q;
        an error occurs if the queue is empty."""
        if self.is_empty():
            raise Empty('Queue is empty')
        first = self.first()
        self._data[self._index_of_first] = None
        self._index_of_first = (self._index_of_first + 1) % len(self._data)
        self._size -= 1

        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)
        return first

    def first(self):
        """Return a reference to the element at the front of queue Q, without removing it;
        an error occurs if the queue is empty"""
        if self.is_empty():
            raise Empty('Queue is empty')
        first_element = self._data[self._index_of_first]
        return first_element

    def is_empty(self):
        """Return True if queue Q does not contain any elements."""
        return self._size == 0

    def _resize(self, cap):
        """Resize to a new list of capacity >= len(self)."""
        old = self._data               # keep track of existing list
        self._data = [None] * cap      # allocate list with new capacity
        walk = self._index_of_first
        for k in range(self._size):    # only consider existing elements
            self._data[k] = old[walk]  # intentionally shift indices
            walk = (1+walk) % len(old)
        self._index_of_first = 0       # front has been realigned

    def __len__(self):
        """Return the number of elements in queue"""
        return self._size

    def __str__(self):
        """Return string version of current queue"""
        return ''.join(str(self._data))
