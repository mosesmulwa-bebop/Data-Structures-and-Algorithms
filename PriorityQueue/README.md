## Explanation
This is a collection of prioritized elements that allows arbitrary element insertion,
and allows the removal of the element that has first priority. When an element is
added to a priority queue, the user designates its priority by providing an associated
key. The element with the minimum key will be the next to be removed from the
queue (thus, an element with key 1 will be given priority over an element with
key 2)

## Priority Queue ADT

Formally, we model an element and its priority as a key-value pair. We define the
priority queue ADT to support the following methods for a 
priority queue P: <bR>
**P.add(k, v):** Insert an item with key k and value v into
priority queue P. <br>
**P.min():** Return a tuple, (k,v), representing the key and value of an
item in priority queue P with minimum key (but do not remove
the item); an error occurs if the priority queue is empty.<bR>
**P.remove min():** Remove an item with minimum key from priority queue P,
and return a tuple, (k,v), representing the key and value of the
removed item; an error occurs if the priority queue is empty. <br>
**P.is empty( ):** Return True if priority queue P does not
contain any items. <br>
**len(P):** Return the number of items in priority queue P.


## Implementation with an unsorted list
For
internal storage, key-value pairs are represented as composites, using instances of
the inherited Item class. These items are stored within a PositionalList, identified
as the data member of our class. We assume that the positional list is implemented
with a doubly-linked list.