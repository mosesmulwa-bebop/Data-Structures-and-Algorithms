class PriorityQueueBase:
    """An abstract base class for implementing a priority queue"""

    class _Item:
        """Lightweight non-public class for storing priority queue items"""
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            """Each item is a key value pair"""
            self._key = k
            self._value = v

        def __lt__(self, other):
            """Used for comparing items. Return True if less than"""
            return self._key < other._key

    def is_empty(self):
        """Return True if there are no elements in queue"""
        return len(self) == 0
    