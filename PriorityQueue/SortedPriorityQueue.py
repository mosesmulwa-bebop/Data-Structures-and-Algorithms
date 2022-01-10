from PositionalLists import PositionalList
from PriorityQueueBase import PriorityQueueBase
from Queue import Empty


class UnsortedPriorityQueue(PriorityQueueBase):                       # base class defines item
    """A min-oriented priority queue implemented with a sorted list"""

    def __init__(self):
        """Create a new priority queue"""
        self._data = PositionalList()

    def __len__(self):
        """Return number of items in priority queue"""
        return len(self._data)

    def _find_min(self):                                            # non-public utility
        """Return position of item with minimum key"""
        if self.is_empty():
            raise Empty('Priority Queue is empty')
        return self._data.first()

    def add(self, key, value):
        """Add a key-value pair"""
        new_item = self._Item(key, value)                           # create new item instance
        walk = self._data.last()                                    # walk backward looking for smaller key
        while walk is not None and new_item < walk.element():
            walk = self._data.before(walk)
        if walk is None:                                            # new key is the smallest
            self._data.add_first(new_item)
        else:
            self._data.add_after(walk, new_item)                    # new item goes after walk

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
