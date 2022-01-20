from HashMapBase import HashMapBase
from Maps_HashTables_and_SkipLists.Maps import UnsortedTableMap


class ChainHashMap(HashMapBase):
    """Hash Map implemented with separate chaining for collision resolution"""
    def _bucket_getitem(self, j, k):
        """This method should search bucket j for an item having key k, returning the
        associated value, if found, or else raising a KeyError"""
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key error: ' + repr(k))          # No match Found
        return bucket[k]                                     # may raise KeyError

    def _bucket_setitem(self, j, k, v):
        """This method should modify bucket j so that key k becomes associated with
        value v. If the key already exists, the new value overwrites the existing value.
        Otherwise, a new item is inserted and this method is responsible for incrementing
        self._n."""
        if self._table[j] is None:
            self._table[j] = UnsortedTableMap()              # create new bucket
        oldsize = len(self._table[j])
        self._table[j][k] = v
        if len(self._table[j]) > oldsize:                    # if key was new to the table
            self._n += 1                                     # increase overall map size

    def _bucket_delitem(self, j, k):
        """This method should remove the item from bucket j having key k, or raise a
        KeyError if no such item exists. (self. n is decremented after this method.)"""
        bucket = self.table[j]
        if bucket is None:
            raise KeyError('KeyError:' + repr(k))  # no match found
        del bucket[k]  # may raise KeyError

    def __iter__(self):
        """This is the standard map method to iterate through all keys of the map."""
        for bucket in self.table:
            if bucket is not None:  # a nonempty slot
                for key in bucket:
                    yield key
