from PositionalLists import PositionalList
from PriorityQueueBase import PriorityQueueBase
from Queue import Empty


class UnsortedPriorityQueue(PriorityQueueBase):                       # base class defines item
    """A min-oriented priority queue implemented with an unsorted list"""

    def __init__(self):
        """Create a new priority queue"""
        self._data = PositionalList()

    def __len__(self):
        """Return number of items in priority queue"""
        return len(self._data)

    def _find_min(self):                                            # non-public utility
        """Return position of item with minimum key"""
        if self.is_empty():                                         # is_empty inherited from base class
            raise Empty('Priority Queue is empty')

        minimum_position = self._data.first()
        walk = self._data.after(minimum_position)

        while walk is not None:
            if walk.element() < minimum_position.element():
                minimum_position = walk
            walk = self._data.after(walk)

        return minimum_position

    def add(self, key, value):
        """Add a key-value pair"""
        new_item = self._Item(key, value)
        self._data.add_last(new_item)

    def min(self):
        """Return but do not remove (k,v) tuple with minimum key"""
        p = self._find_min()
        item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        """Remove and return (k,v) tuple with minimum key"""
        p = self._find_min()
        item = self._data.delete(p)
        return (item._key, item._value)
