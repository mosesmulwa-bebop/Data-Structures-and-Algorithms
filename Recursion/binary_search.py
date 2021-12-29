def binary_search(data, target, low, high):
    """Return true if target is found in indicated portion of a python list
    The search only considers the portion from data[low] to data[high] inclusive
    """
    if low > high:
        return False                        # interval is empty,no match
    else:
        mid = int((low+high)/2)
        if target == data[mid]:
            return True
        elif target < data[mid]:
            # recur on portion left of middle
            return binary_search(data, target, low, mid-1)
        else:
            # recur on portion right of middle
            return binary_search(data, target, mid+1, high)


mylist = [2, 4, 5, 7, 8, 9, 12, 13, 16, 17, 19, 21, 23, 26]

print(binary_search(mylist, 8, 0, len(mylist)))

