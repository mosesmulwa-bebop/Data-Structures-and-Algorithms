from BinaryTree import BinaryTree


class LinkedBinaryTree(BinaryTree):
    """Linked implementation of a binary tree"""

    # ----------------------non public node class ------------------------
    class _Node:
        """Abstraction representing a single node"""
        __slots__ = '_element','_parent', '_left', '_right'

        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    # -----Position class with methods now implemented -----------------
    class Position(BinaryTree.Position):
        """An abstraction representing the location of a single element"""

        def __init__(self, container, node):
            """Constructor should not be invoked by the user"""
            self._container = container
            self._node = node

        def element(self):
            """Return element stored in the node located in this position"""
            return self._node.element

        def __eq__(self, other):
            """Return True if other position represents the same location"""

            return type(self) is type(other) and self._node is other._node

    # ------------------ utility methods ------------------------------
    def _validate(self, p):
        """Determine if p is a valid position and
        return node stored in position p if it is valid"""

        if not isinstance(p, self.Position):
            raise TypeError('Must be of type position')
        if p._container is not self:
            raise ValueError('Position does not belong to this container')
        if p._node._parent is p._node:           # convention for deprecated nodes
            raise ValueError('Position is not valid and contains deprecated node')
        return p._node

    def _make_position(self, node):
        """Return Position instance for given node (or None if no node)"""
        if node is None:
            return None
        new_position = self.Position(self, node)
        return new_position

    # -----------------------linked binary tree ------------------

    def __init__(self):
        """Create an initially empty binary tree"""
        self._root = None
        self._size = 0

    # ---------------------Public Accessors --------------------
    def root(self):
        """Return position representing the root of the tree"""
        return self._make_position(self._root)

    def parent(self, p):
        """Return position of parent of p or None if no parent"""
        node_at_position_p = self._validate(p)
        return self._make_position(node_at_position_p._parent)

    def num_children(self, p):
        """Return number of children of position p"""
        count = 0
        node_at_position_p = self._validate(p)
        if node_at_position_p._left is not None:
            count += 1
        if node_at_position_p._right is not None:
            count += 1
        return count

    def __len__(self):
        """Return number of positions stored in tree"""
        return self._size

    def left(self, p):
        """Return the position of the left child of position p
        or None if there is no left child"""
        node_at_position_p = self._validate(p)
        return self._make_position(node_at_position_p._left)

    def right(self, p):
        """Return the position of the right child of position p
                or None if there is no right child"""
        node_at_position_p = self._validate(p)
        return self._make_position(node_at_position_p._right)

    # ---------------------Non public mutators----------------------------

    def _add_root(self, e):
        """Place element e at root of tree and return the position of the root"""
        if self._root is not None:
            raise ValueError('Root already exists')
        new_node = self._Node(e)
        self._root = new_node
        self._size = 1
        return self._make_position(self._root)

    def _add_left(self, p, e):
        """Place element e as left child of node at position p and return position"""
        node_at_position_p = self._validate(p)
        if node_at_position_p._left is not None:
            raise ValueError('Left child at given position already exists')
        new_node = self._Node(e)
        new_node._parent = node_at_position_p
        node_at_position_p._left = new_node
        self._size += 1
        return self._make_position(new_node)

    def _add_right(self, p, e):
        """Place element e as right child of node at position p and return position"""
        node_at_position_p = self._validate(p)
        if node_at_position_p._right is not None:
            raise ValueError('Right child at given position already exists')
        new_node = self._Node(e)
        new_node._parent = node_at_position_p
        node_at_position_p._right = new_node
        self._size += 1
        return self._make_position(new_node)

    def _replace(self, p, e):
        """Replace element at position p with element e and return old element"""
        node_at_position_p = self._validate(p)
        old_element = node_at_position_p._element
        node_at_position_p._element = e
        return old_element

    def _delete(self, p):
        """Delete node at position p and replace it with its child if any

        Return the element stored at position p
        Raise ValueError if p is invalid or p has two children
        """

        node_at_position_p = self._validate(p)
        if self.num_children(node_at_position_p) == 2:
            raise ValueError('Position has two children')

        # one of the left or right nodes has to be the child, it can also have no children
        child = node_at_position_p._left if node_at_position_p._left else node_at_position_p._right  # might be None

        if child is not None:
            child._parent = node_at_position_p._parent                  # child's grandparent becomes parent

        if node_at_position_p is self._root:
            self._root = child                                          # child becomes root
        else:
            parent = node_at_position_p._parent
            if parent._left is node_at_position_p:
                parent._left = child
            else:
                parent._right = child

        self._size -= 1
        node_at_position_p._parent = node_at_position_p                 # convention for deprecated node
        return node_at_position_p._element

    def _attach(self, p, t1, t2):
        """Attach trees t1 and t2 as left and right subtrees of position p"""
        node_at_position_p = self._validate(p)

        if not self.is_leaf(p):
            raise ValueError('Position p not a leaf')
        if not type(self) is type(t1) is type(t2):
            raise TypeError('Tree types must match')

        self._size = self._size + len(t1) + len(t2)
        if not t1.is_empty():

            node_at_root_of_t1 = t1._root
            node_at_position_p._left = node_at_root_of_t1
            node_at_root_of_t1._parent = node_at_position_p
            # deprecate t1
            t1._root = None
            t1._size = 0
        if not t2.is_empty():

            node_at_root_of_t2 = t2._root
            node_at_position_p._right = node_at_root_of_t2
            node_at_root_of_t2._parent = node_at_position_p
            # deprecate t2
            t2._root = None
            t2._size = 0








