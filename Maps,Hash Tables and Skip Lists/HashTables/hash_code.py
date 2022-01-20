def hash_code(s):
    """Cyclic shift hash code computation for a character string"""
    mask = (1 << 32) - 1           # mask of 32 bits of 1 to ensure limit is 32-bit integers
    h = 0                          # hash code

    for character in s:
        h = (h << 5 & mask) | (h >> 27)    # 5-bit cyclic shift of running sum
        h += ord(character)                # add in value of next character
        return h


# -------------------- more intuitive example--------------------
mask = (1 << 32) - 1
h = 0b10111101100101101010100010101000
print("Original Hash: ", bin(h))
print("Shifted to left 5 times: ", bin(h << 5))
print("Mask: ", bin(mask))
print("ANDed with mask: ", bin(h <<5 & mask))
print("Original hash shifted to the right 27: ", bin(h >> 27))
h = (h << 5 & mask) | (h >> 27)
print("After ORing with 27 right shift: ", bin(h))
