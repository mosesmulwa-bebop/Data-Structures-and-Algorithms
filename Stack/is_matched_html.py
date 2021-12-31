from ArrayStack import ArrayStack


def is_matched_html(raw):
    """Function to determine if all HTML tags are properly matched. Uses a stack to implement this"""

    S = ArrayStack()                                       # Create empty stack
    j = raw.find('<')                                      # find first < character

    while j != -1:
        k = raw.find('>')                                  # find next '> character
        if k == -1:
            return False
        tag = raw[j+1:k]                                  # get tag

        if not tag.startswith('/'):                       # opening tag
            S.push(tag)
        else:                                             # closing tag
            if S.is_empty():                              # nothing to compare with
                return False
            if tag[1:] != S.pop():                        # compare with what is in stack
                return False
        j = raw.find('<', k + 1)                          # find next '<' character

    return S.is_empty()                                   # were all opening tags matched?




