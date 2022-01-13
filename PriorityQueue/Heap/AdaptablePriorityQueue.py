from HeapPriorityQueue import HeapPriorityQueue


class AdaptablePriorityQueue(HeapPriorityQueue):
    """A locator based priority queue implemented with a binary heap"""

    # ---------------------------nested Locator class -----------------------------
    class Locator(HeapPriorityQueue._Item):
        """Token for locating an entry of the priority queue"""

        __slots__ = '_index'                            # add additional field index

        def __init__(self, k, v, j):
            super.__init__(k, v)
            self._index = j

    # ------------------------non Public Behaviours-------------------------------
    # override swap to record new indices
    def _swap(self, i, j):
        super()._swap(i, j)                 # perform swap
        # update new indices for locators
        self._data[i]._index = i
        self._data[j]._index = j

    def _bubble(self, j):
        """Determine whether to upheap or downheap from index j"""
        if j > 0 and self._data[j] < self._data[self._parent[j]]:
            self._upheap(j)
        else:
            self._downheap(j)

    # --------------------------Public methods---------------------------------
    def add(self, key, value):
        """Add a key value pair and return its locator"""
        # create new token
        # index of locator will be current last index plus one
        # Thus it is len(self._data)
        token = self.Locator(key, value, len(self._data))
        # add to back of queue
        self._data.append(token)
        # call upheap from this index. Recall current index is now length -1 like normal
        self._upheap(len(self._data) - 1)
        return token

    def update(self, loc, newkey, newval):
        """Update the key and value for the entry identified by Locator loc"""
        # first,detemine if locator is valid
        j = loc._index
        if not(0 <= j <= len(self) and self._data[j] is loc):
            raise ValueError('Locator is not valid')
        loc._key = newkey
        loc._value = newval
        self._bubble(j)

    def remove(self, loc):
        """Remove and return key,value pair identified by locator loc"""
        # first,detemine if locator is valid
        j = loc._index
        if not (0 <= j <= len(self) and self._data[j] is loc):
            raise ValueError('Locator is not valid')
        # if last index
        if j == len(self):
            self._data.pop()
        else:
            # replace locator with the last one
            self._swap(j, len(self))
            self._data.pop()
            self._bubble(j)
        return (loc._key, loc._value)
