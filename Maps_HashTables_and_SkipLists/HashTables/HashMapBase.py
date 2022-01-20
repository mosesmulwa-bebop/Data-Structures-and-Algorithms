from random import randrange

from Maps_HashTables_and_SkipLists.Maps import MapBase


class HashMapBase(MapBase):
    """Abstract base class for map using hash table with MAD compression"""

    def __init__(self, cap=11, p=109345121):
        """Create an empty hash table map"""
        self._table = cap * [None]          # empty list of size capacity
        self._n = 0                         # number of entries in map
        self._prime = p                     # prime for MAD compression
        self._scale = 1 + randrange(p - 1)  # scale from 1 to p-1 for MAD
        self._shift = randrange(p)          # scale from 0 to p-1 for MAD

    def _hash_function(self, k):
        """Return index given key k"""
        return (hash(k) * self._scale + self._shift) % self._prime % len(self._table)

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        j = self._hash_function(k)
        return self._bucket_getitem(j, k)            # may raise key error

    def __setitem__(self, k, v):
        j = self._hash_function(k)
        self._bucket_setitem(j, k, v)                # subroutine maintains self._n
        if self._n > len(self._table) // 2:          # keep load factor <= 0.5
            self._resize(2 * len(self._table) - 1)   # number 2^x - 1 is often prime

    def __delitem__(self, k):
        j = self._hash_function(k)
        self._bucket_delitem(j, k)                   # may raise key error
        self._n -= 1

    def _resize(self, c):
        """Resize bucket array to capacity c"""
        old = list(self.items())                      # get iteration of all items in map
        self._table = c * [None]                      # create new empty map
        self._n = 0                                   # reset number of elements
        for (k, v) in old:
            self[k] = v                               # reinsert old key-value pair,n recomputed during subsequent adds

    # ----------abstract methods that concrete subclass must support-------

    def _bucket_getitem(self, j, k):
        """This method should search bucket j for an item having key k, returning the
        associated value, if found, or else raising a KeyError"""
        raise NotImplementedError('must be implemented by subclass')

    def _bucket_setitem(self, j, k, v):
        """This method should modify bucket j so that key k becomes associated with
        value v. If the key already exists, the new value overwrites the existing value.
        Otherwise, a new item is inserted and this method is responsible for incrementing
        self._n."""
        raise NotImplementedError('must be implemented by subclass')

    def _bucket_delitem(self, j, k):
        """This method should remove the item from bucket j having key k, or raise a
        KeyError if no such item exists. (self. n is decremented after this method.)"""
        raise NotImplementedError('must be implemented by subclass')

    def __iter__(self):
        """This is the standard map method to iterate through all keys of the map."""
        raise NotImplementedError('must be implemented by subclass')

