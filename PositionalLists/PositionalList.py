from _DoublyLinkedBase import _DoublyLinkedBase


class PositionalList(_DoublyLinkedBase):
    """A sequential container of elements allowing positional access."""

    #  ------------------------nested Position class-------------------#
    class Position:
        """An abstraction representing the location of a single element"""

        def __init__(self, container, node):
            """Constructor should not be invoked by the user"""
            self._container = container
            self._node = node

        def element(self):
            """Return element stored at this position"""
            return self._node.element

        def __eq__(self, other):
            """Return True if other is a position representing the same location"""
            return type(self) is type(other) and self._node is other._node

        def __ne__(self, other):
            """Return True if other does not represent the same location"""
            return not (self == other)

    # ------------------------------utility methods--------------------
    def _validate(self, p):
        """Return position's node or raise appropriate error if invalid"""
        if not isinstance(p, self.Position):
            raise TypeError('p must be of the type Position')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node.next_node is None:                   # convention for deprecated nodes
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        """Return position instance for a given node(or None if sentinel)"""
        if node is self._header or node is self._trailer:
            return None                                 # boundary violation
        else:
            return self.Position(self, node)            # legitimate position

    # ----------------------------accessors----------------------------------
    def first(self):
        """Return first position in the list(or None if list is empty)"""
        return self._make_position(self._header.next_node)

    def last(self):
        """Return last position in the list(or None if list is empty)"""
        return self._make_position(self._trailer.prev_node)

    def before(self, p):
        """Return position before position p (or None if p is first)"""
        node_at_position_p = self._validate(p)
        return self._make_position(node_at_position_p.prev_node)

    def after(self, p):
        """Return position after position p (or None if p is last)"""
        node_at_position_p = self._validate(p)
        return self._make_position(node_at_position_p.next_node)

    def __iter__(self):
        """Generate a forward iteration of the elements of the list"""
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    # ------------------------mutators---------------------------------
    # override inherited version to return a position instead of a node
    def _insert_between(self, e, predecessor, successor):
        """Add element between existing nodes and return new position"""
        mynode = super()._insert_between(e, predecessor, successor)
        return self._make_position(mynode)

    def add_first(self, e):
        """insert element e at front of list and return the position"""
        return self._insert_between(e, self._header, self._header.next_node)

    def add_last(self, e):
        """insert element e at back of list and return the position"""
        return self._insert_between(e, self._trailer.prev_node, self._trailer)

    def add_before(self, p, e):
        """Add element e before position p and return the position"""
        node_at_position_p = self._validate(p)
        return self._insert_between(e, node_at_position_p.prev_node, node_at_position_p)

    def add_after(self, p, e):
        """Add element e after position p and return the position"""
        node_at_position_p = self._validate(p)
        return self._insert_between(e, node_at_position_p, node_at_position_p.next_node)

    def delete(self, p):
        """Return and remove element at position p"""
        node_at_position_p = self._validate(p)
        return self._delete_node(node_at_position_p)

    def replace(self, p, e):
        """Replace the element at position p with element e,
        returning the element formerly at position p."""
        node_at_position_p = self._validate(p)
        old_element = node_at_position_p.element
        node_at_position_p.element = e
        return old_element
