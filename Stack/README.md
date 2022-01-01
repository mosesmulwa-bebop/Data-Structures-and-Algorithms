## Explanation
A stack is a collection of objects that are inserted and removed according to the
last-in, first-out (LIFO) principle. A user may insert objects into a stack at any
time, but may only access or remove the most recently inserted object that remains
(at the so-called “top” of the stack).

Formally, a stack is an abstract
data type (ADT) such that an instance S supports the following two methods:<br>
S.push(e): Add element e to the top of stack S. <br>
S.pop(): Remove and return the top element from the stack S;
an error occurs if the stack is empty.
<br>
Additionally, we define the following accessor methods for convenience:<br>
S.top(): Return a reference to the top element of stack S, without
removing it; an error occurs if the stack is empty.<br>
S.is empty( ): Return True if stack S does not contain any elements. <br>
len(S): Return the number of elements in stack S; in Python, we
implement this with the special method len .
