from HashMapBase import HashMapBase


class ProbeHashMap(HashMapBase):
    """Hash Map implemented with Linear Probing for conflict resolution"""
    _AVAIL = object()                                        # sentinel marks locations of previous deletions

    def _is_available(self, j):
        """Return True if index j is available in the table"""
        return self._table[j] is None or self._table[j] is ProbeHashMap._AVAIL

    def _find_slot(self, j, k):
        """Search for key k in bucket starting at j

        Return (success, index) tuple:
        If match was found, success is True, index denotes location
        If no match found, success is False, index denotes first available Location
        """

        first_avail = None
        while True:
            if self._is_available(j):
                if first_avail is None:
                    first_avail = j                         # set this as the first available location
                if self._tabel[j] is None:
                    return (False, first_avail)
            elif k == self._table[j]._key:
                return (True, j)                            # found a match

            j = (j+1) % len(self._table)                    # keep probing (cyclical linear shift)

    def _bucket_getitem(self, j, k):
        """This method should search bucket j for an item having key k, returning the
        associated value, if found, or else raising a KeyError"""
        found, s = self._find_slot(j, k)
        if not found:
            raise KeyError('Key error: ' + repr(k))
        return self._table[s]._value

    def _bucket_setitem(self, j, k, v):
        """This method should modify bucket j so that key k becomes associated with
        value v. If the key already exists, the new value overwrites the existing value.
        Otherwise, a new item is inserted and this method is responsible for incrementing
        self._n."""
        found, s = self._find_slot(j, k)
        if not found:
            self._table[s] = self._Item(k, v)               # insert new item
            self._n += 1                                    # increase size
        else:
            self._table[s]._value = v                       # overwrite existing one

    def _bucket_delitem(self, j, k):
        """This method should remove the item from bucket j having key k, or raise a
        KeyError if no such item exists. (self._n is decremented after this method.)"""
        found, s = self._find_slot(j, k)
        if not found:
            raise KeyError('Key error: ' + repr(k))         # no match found

        self._table[s] = ProbeHashMap._AVAIL                # mark as vacated

    def __iter__(self):
        """This is the standard map method to iterate through all keys of the map."""
        for j in range(len(self._table)):
            if not self._is_available(j):                   # if there exists an item
                yield self._table[j]._key
