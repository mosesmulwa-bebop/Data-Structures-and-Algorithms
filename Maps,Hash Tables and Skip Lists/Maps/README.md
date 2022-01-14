
## Explanation
It represents an abstraction in which unique keys are mapped
to associated values.

![Map](map.PNG)

## The Map ADT
We begin by listing what we consider the
most significant five behaviors of a map M as follows: <br>
**M[k]:** Return the value v associated with key k in map M, if
one exists; otherwise raise a KeyError. In Python, this is
implemented with the special method getitem . <br>
**M[k] = v:** Associate value v with key k in map M, replacing the existing
value if the map already contains an item with key
equal to k. In Python, this is implemented with the special
method setitem .<br>
**del M[k]:** Remove from map M the item with key equal to k; if M
has no such item, then raise a KeyError. In Python, this is
implemented with the special method delitem . <br>
**len(M):** Return the number of items in map M. In Python, this is
implemented with the special method len .<br>
**iter(M):** The default iteration for a map generates a sequence of
keys in the map. In Python, this is implemented with the
special method iter , and it allows loops of the form,
for k in M.

For additional convenience,
map M should also support the following behaviors: <br>
**k in M:** Return True if the map contains an item with key k. In
Python, this is implemented with the special contains
method. <br>
**M.get(k, d=None):** Return M[k] if key k exists in the map; otherwise return
default value d. This provides a form to query M[k] without
risk of a KeyError.<br>
**M.setdefault(k, d):** If key k exists in the map, simply return M[k]; if key k
does not exist, set M[k] = d and return that value.<br>
**M.pop(k, d=None):** Remove the item associated with key k from the map and
return its associated value v. If key k is not in the map,
return default value d (or raise KeyError if parameter d is
None).<br>

**M.popitem():** Remove an arbitrary key-value pair from the map, and return
a (k,v) tuple representing the removed pair. If map is
empty, raise a KeyError.<br>
**M.clear( ):** Remove all key-value pairs from the map.<br>
**M.keys( ):** Return a set-like view of all keys of M.<br>
**M.values( ):** Return a set-like view of all values of M.<br>
**M.items( ):** Return a set-like view of (k,v) tuples for all
entries of M.<br>
**M.update(M2):** Assign M[k] = v for every (k,v) pair in map M2.<br>
**M == M2:** Return True if maps M and M2 have identical key-value
associations.<br>
**M != M2:** Return True if maps M and M2 do not have identical keyvalue
associations.<br>