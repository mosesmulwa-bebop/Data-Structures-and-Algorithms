class _Node:
    """Lightweight, non-public class for storing a single linked list node"""
    __slots__ = 'element', 'next_node'             # streamline memory usage

    def __init__(self, element, next_node):
        self.element = element                      # reference to user's element
        self.next_node = next_node                  # reference to next node



