def linear_sum(S, n):
    """Returns the sum of the first n terms in Sequence S
    """
    if n == 0:
        return 0
    else:
        return linear_sum(S, n-1) + S[n-1]


mylist = [2, 4, 5, 7, 8, 9, 12, 13, 16, 17, 19, 21, 23, 26]
print(linear_sum(mylist, len(mylist)))
