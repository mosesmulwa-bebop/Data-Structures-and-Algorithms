def binary_sum(S, start, stop):
    """Return the sum of numbers in implicit slice S[start:stop].

    we can recursively compute the sum of the first half, and the sum of the second half, and add these sums
    together.
    """
    if start >= stop:  # zero elements in slice
        return 0
    elif start == stop - 1:    # one element in slice
        return S[start]
    else:                      # two or more elements in slice
        mid = int((start+stop)/2)
        return binary_sum(S, start, mid) + binary_sum(S, mid, stop)


mylist = [2, 4, 5, 7, 8, 9, 12, 13, 16, 17, 19, 21, 23, 26]
print(binary_sum(mylist, 0, len(mylist)))
