## Explanation
The queue abstract data type defines a collection that keeps 
objects in a sequence, where element access and deletion are 
restricted to the first element in the queue, and element 
insertion is restricted to the back of the sequence. <br>
This restriction enforces the rule that items are inserted and deleted in a queue according
to the <b> first-in, first-out (FIFO) principle</b>.<br>
The queue abstract data type (ADT) supports the following two 
fundamental methods for a queue Q: <br>
**Q.enqueue(e):** Add element e to the back of queue Q. <br>
**Q.dequeue():** Remove and return the first element from queue Q;
an error occurs if the queue is empty. <br>
The queue ADT also includes the following supporting methods : <br>
**Q.first():** Return a reference to the element at the front of queue Q,
without removing it; an error occurs if the queue is empty. <br>
**Q.is empty( ):** Return True if queue Q does not contain any 
elements. <br>
**len(Q):** Return the number of elements in queue Q; in Python,
we implement this with the special method len .

### Implemetation using circular array
We allow the front of the queue to drift rightward,
and we allow the contents of the queue to “wrap around” 
the end of an underlying array. We assume that our underlying array has fixed length N
that is greater that the actual number of elements in the queue. New elements
are enqueued toward the “end” of the current queue, progressing from the front to
index N −1 and continuing at index 0, then 1.

### Resizing the queue
When enqueue is called at a time when the size of the queue equals the size of the
underlying list, we rely on a standard technique of doubling the storage capacity of
the underlying list

### Shrinking the underlying array
Reduce the array to half of its current size, whenever the number of elements
stored in it falls below one fourth of its capacity