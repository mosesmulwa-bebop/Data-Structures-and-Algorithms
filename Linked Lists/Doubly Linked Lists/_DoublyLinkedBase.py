from Node import _Node as Node


class _DoublyLinkedBase:
    """a non-public class for implementing doubly linked lists"""

    def __init__(self):
        """Create an empty list"""
        self._header = Node(None, None, None)               # create new header node
        self._trailer = Node(None, None, None)              # create new trailer node
        self._header.next_node = self._trailer              # next node after header is trailer
        self._trailer.prev_node = self._header
        self._size = 0                                      # number of nodes in list

    def __len__(self):
        """Return number of elements in list"""
        return self._size

    def is_empty(self):
        """Return true if list is empty"""
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        """Insert node with element e between predecessor and successor nodes and return new node"""
        new_node = Node(e, predecessor, successor)
        predecessor.next_node = new_node
        successor.prev_node = new_node
        self._size += 1
        return new_node



    def _delete_node(self, node):
        """Delete non-sentinel node from the list and return its element"""
