class _Node:
    """Lightweight, non-public class for a doubly linked list node"""
    __slots__ = "element", "prev_node", "next_node"               # streamline memory

    def __init__(self, element, prev_node, next_node):
        self.element = element                                    # element to be stored
        self.prev_node = prev_node                                # previous node reference
        self.next_node = next_node                                # next node reference
