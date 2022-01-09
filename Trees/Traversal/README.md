## Explanation

A traversal of a tree T is a systematic way of accessing, or “visiting,” all the positions
of T.

## Traversal of General Tress
## 1. Preorder traversal
In a preorder traversal of a tree T, the root of T is visited first and then the subtrees
rooted at its children are traversed recursively

Algorithm preorder(T, p):<br>
**    **perform the “visit” action for position p<br>
**    **for each child c in T.children(p) do: <br>
****  ****preorder(T, c) {recursively traverse the subtree rooted at c}

![Pre Order Traversal](PreOrder.PNG)

## 2. Postorder traversal
It recursively traverses the subtrees rooted at the children of the root first, and
then visits the root (hence, the name “postorder”).

Algorithm postorder(T, p): <bR>
** **for each child c in T.children(p) do:<br>
****** **postorder(T, c) {recursively traverse the subtree rooted at c}<bR>
** **perform the “visit” action for position p

![PostOrder Traversal](PostOrder.PNG)

## 3. Breadth-first traversal
It traverses a tree so that we visit
all the positions at depth d before we visit the positions 
at depth d +1.

We use a queue to produce a FIFO (i.e., first-in first-out) 
semantics for the order in which
we visit nodes. <br>
The overall running time is O(n), due to the n calls to 
enqueue and 
n calls to dequeue. <br>

Algorithm breadth_first(T): <br>
Initialize queue Q to contain T.root() <bR>
while Q not empty do: <br>
  **   **  p = Q.dequeue( ) {p is the oldest entry in the queue} <br>
 **   **   perform the “visit” action for position p <bR>
 **   **  for each child c in T.children(p) do: <br>
 **   **   **   **  Q.enqueue(c) {add p’s children to the end of
the queue for later visits}

![Breadth First Traversal](Breadthfirst.PNG)

## Traversal of Binary Trees
## 1. Inorder Traversal
The inorder traversal of a binary tree T can be
informally viewed as visiting the nodes of T “from left to right.” Indeed, for every
position p, the inorder traversal visits p after all the positions in the left subtree of
p and before all the positions in the right subtree of p.

Basically : left subtree, current position, right subtree

Algorithm inorder(p): <br>
  ** **  if p has a left child lc then: <br>
**       ****      **inorder(lc) {recursively traverse the 
left subtree of p} <br>
**  **perform the “visit” action for position p <br>
** **if p has a right child rc then: <br>
****  ****inorder(rc) {recursively traverse the right subtree of p}

![Inorder Traversal](InOrder.PNG)


## Implementation
The file Tree.py copies the original tree.py and implements
the traversal methods.
The file BinaryTree.py implements the inorder traversal