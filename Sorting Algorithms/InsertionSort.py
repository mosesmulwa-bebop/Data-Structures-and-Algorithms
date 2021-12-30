def insertion_sort(A):
    """Sort list of comparable elements into non-decreasing order"""
    for k in range(1, len(A)):
        cur = A[k]                                        # Current element to be inserted
        j = k                                             # find correct index j for current

        while j > 0 and A[j-1] > cur:                     # element A[j-1] (left) must be greater than current
            A[j] = A[j-1]
            j -= 1

        A[j] = cur                                        # cur is now in the right place


mylist = [3, 4, 67, 2, 1, 11, 56, 34]
print("Before sort: " + str(mylist))
insertion_sort(mylist)
print("After sort: " + str(mylist))
