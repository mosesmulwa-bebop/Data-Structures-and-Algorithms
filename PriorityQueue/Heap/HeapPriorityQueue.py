from PriorityQueue import PriorityQueueBase


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

    def __len__(self):
        """Return number of items in queue"""
        return len(self._data)

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



