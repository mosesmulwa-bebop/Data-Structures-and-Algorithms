## This repo covers various sorting Algorithms

## 1. Insertion sort
The algorithm proceeds as follows for an array based
sequence. We start with the first element in the array. One element by itself
is already sorted. Then we consider the next element in the array. If it is smaller
than the first, we swap them. Next we consider the third element in the array. We
swap it leftward until it is in its proper order with the first two elements. We then
consider the fourth element, and swap it leftward until it is in the proper order with
the first three. We continue in this manner with the fifth element, the sixth, and so
on, until the whole array is sorted.

### Pseudocode
Input: An array A of n comparable elements

Output: The array A with elements rearranged in 
nondecreasing order

for k from 1 to n − 1 do:

    Insert A[k] at its proper location within A[0], A[1], . . ., A[k].

### Analysis
The nested loops of insertion-sort lead to an O(n^2) running time in the worst
case. The most work is done if the array is initially in reverse order. On the other
hand, if the initial array is nearly sorted or perfectly sorted, insertion-sort runs in
O(n) time because there are few or no iterations of the inner loop. 