import ctypes              # Provides low-level Arrays


class DynamicArray:
    """A dynamic array class akin to a simplified Python list

    n -> The number of actual elements currently stored in the list.
    capacity ->  The maximum number of elements that could be stored in the currently allocated array.
    A -> The reference to the currently allocated array
    """
    def __init__(self):
        """Create an empty array
        """
        self._n = 0                                  # Count actual elements
        self._capacity = 1                           # Default array capacity
        self._A = self._make_array(self._capacity)   # Low-level Array

    def __len__(self):
        """Return number of elements stored in the array
        """
        return self._n

    def __getitem__(self, k):
        """Return element at index k
        """
        if not 0 <= k <= self._n:
            raise IndexError('invalid index')       # if k is outside index of A
        return self._A[k]

    def append(self, obj):
        """Add object to end of array
        """
        if self._n == self._capacity:               # if the array is full, not enough room
            self._resize(2 * self._capacity)        # Basically make array twice the current size
        self._A[self._n] = obj                      # add element to position n
        self._n += 1                                # increase number of elements

    def _resize(self, c):                           # Non-public utility
        """Resize internal array to capacity c
        """
        B = self._make_array(c)                     # Make array B with capacity c
        for k in range(self._n):
            B[k] = self._A[k]                       # Copy existing values to new Array
        self._A = B                                 # Use the bigger Array
        self._capacity = c                          # Set new capacity as c

    def _make_array(self, c):
        """Return new array with capacity c
        """
        return (c * ctypes.py_object)()
