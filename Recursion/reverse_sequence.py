def reverse_sequence(S, start, stop):
    """Reverse the elements of slice S[start:stop]
    """
    if start < stop-1:    # at least two elements
        S[start], S[stop-1] = S[stop-1], S[start]  # swap first and last
        reverse_sequence(S, start+1, stop-1)  # recur on the rest


mylist = [2, 4, 5, 7, 8, 9, 12, 13, 16, 17, 19, 21, 23, 26]
print(mylist)
reverse_sequence(mylist, 0, len(mylist))
print(mylist)

