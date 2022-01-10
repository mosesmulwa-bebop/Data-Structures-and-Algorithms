from PriorityQueue import PriorityQueueBase
from Queue import Empty


class HeapPriorityQueue(PriorityQueueBase):                            # base class defines _item
    """Heap implementation of a priority queue using a list as underlying storage"""

    def __init__(self):
        self._data = []                                                 # initialize empty list

    # -------------------------------Non public utility methods------------------

    def _parent(self, j):
        """Return index of the parent of j"""
        return (j-1)//2

    def _left(self, j):
        """Return index of Left child of j"""
        return 2*j + 1

    def _right(self, j):
        """Return index of Right child of j"""
        return 2*j + 2


    def _has_left(self, j):
        """Return True if j has a left child"""
        return self._left(j) < len(self)                        # will be False if index out of range

    def _has_right(self, j):
        """Return True if j has a right child"""
        return self._right(j) < len(self)                        # will be False if index out of range

    def _swap(self, i, j):
        """Swap item at index i with that at j"""
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self, j):
        """Perform up heap bubble from index j"""
        parent = self._parent(j)

        if j > 0 and self._data[parent] < self._data[j]:
            self._swap(parent, j)
            self._upheap(parent)

    def _downheap(self, j):
        """Perform down heap from index j"""
        if self._has_left(j):
            left = self._left(j)
            smallest_child = left
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] < self._data[left]:
                    smallest_child = right
            if self._data[smallest_child] < self._data[j]:
                self._swap(j, smallest_child)
                self._downheap(smallest_child)

    # -----------------------------------Public Behaviours----------------------------------------

    def __len__(self):
        """Return number of items in queue"""
        return len(self._data)

    def add(self, key, value):
        """Add key value pair to tree"""
        new_item = self._Item(key, value)           # create new item
        self._data.append(new_item)                 # add item to back of list
        last_index = len(self) - 1
        self._upheap(last_index)                    # perform upheap bubbling from last index

    def min(self):
        """Return key value tuple of the minimum"""
        if self.is_empty:
            raise Empty('Priority Queue is Empty')
        item = self._data[0]                        # minimum is at the root
        return (item._key, item._value)

    def remove_min(self):
        """Return and remove minimum"""
        if self.is_empty:
            raise Empty('Priority Queue is Empty')
        last_index = len(self) - 1
        self._swap(0, last_index)                   # swap items at root and last index
        item = self._data.pop()                     # remove and return item at last index
        self._downheap(0)                           # perform down heap bubbling from index 0
        return (item._key, item._value)

