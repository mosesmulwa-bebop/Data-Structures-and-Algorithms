def insertion_sort(L):
    """Sort Positional list of comparable elements into non-decreasing order"""
    if len(L) > 1:                              # otherwise, no need to sort it
        marker = L.first()
        while marker != L.last():
            pivot = L.after(marker)             # position right of marker, the next item to place
            value = pivot.element()
            if value > marker.element():        # pivot already sorted
                marker = pivot                  # pivot becomes new marker
            else:                               # not sorted, must relocate pivot
                walk = marker                   # find leftmost item greater than value
                while walk != L.first() and L.before(walk).element() > value:
                    walk = L.before(walk)
                L.delete(pivot)
                L.add_before(walk, value)       # reinsert value before walk


