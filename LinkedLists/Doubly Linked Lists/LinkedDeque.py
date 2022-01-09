from _DoublyLinkedBase import _DoublyLinkedBase
from Node import _Node as Node
from Empty import Empty


class LinkedDeque(_DoublyLinkedBase):                               # inherits from the doubly linked base class
    """Double ended queue implementation using a doubly linked list"""

    def first(self):
        """Return but do not remove the element at the front of the queue"""
        if self.is_empty():
            raise Empty('Queue is empty!')
        mynode = self._header.next_node
        return mynode.element

    def last(self):
        """Return but do not remove the element at the back of the queue"""
        if self.is_empty():
            raise Empty('Queue is empty!')
        mynode = self._trailer.prev_node
        return mynode.element

    def insert_first(self, e):
        """insert node with element e at the front of the queue"""
        self._insert_between(e, self._header, self._header.next_node)

    def insert_last(self, e):
        """insert node with element e at the back of the queue"""
        self._insert_between(e, self._trailer.prev_node, self._trailer)

    def delete_first(self):
        """Remove and return element at front of queue"""
        self._delete_node(self._header.next_node)

    def delete_last(self):
        """Remove and return element at back of queue"""
        self._delete_node(self._trailer.prev_node)



