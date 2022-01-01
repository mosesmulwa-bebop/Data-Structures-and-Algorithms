## Explanation
This is a queue-like data structure that supports insertion and deletion
at both the front and the back of the queue.

The deque ADT is defined so that deque D
supports the following methods:<br>
**D.add first(e)**: Add element e to the front of deque D.<br>
**D.add last(e):** Add element e to the back of deque D.<br>
**D.delete first( ):** Remove and return the first element from deque D;
an error occurs if the deque is empty.<br>
**D.delete last( ):** Remove and return the last element from deque D;
an error occurs if the deque is empty.<br>

Additionally, the deque ADT will include the following 
accessors:<br>
**D.first():** Return (but do not remove) the first element of deque D;
an error occurs if the deque is empty.<br>
**D.last():** Return (but do not remove) the last element of deque D;
an error occurs if the deque is empty.<br>
**D.is empty( ):** Return True if deque D does not contain 
any elements.<br>
**len(D):** Return the number of elements in deque D; in Python,
we implement this with the special method len .<br>

### Implementation
It is implemented using a circular array.Check the Queue Readme 
for more details on circular array implementation