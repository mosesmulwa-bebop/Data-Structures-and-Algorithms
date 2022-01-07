class Tree:
    """An abstract base class representing a tree"""

    # ------nested Position class------------
    class Position:
        """An abstraction representing the location of a single element"""

        def element(self):
            """Return element stored at this position"""
            raise NotImplementedError('must be implemented by subclass')

        def __eq__(self, other):
            """Return True if other position represents the same location"""
            raise NotImplementedError('must be implemented by subclass')

        def __ne__(self, other):
            """Return True if other position is not the same location"""
            return not(self == other)

    # ----------abstract methods that concrete subclass must support-------
    def root(self):
        """Return position representing the root of the tree"""
        raise NotImplementedError('must be implemented by subclass')

    def parent(self, p):
        """Return position of parent of p or None if no parent"""
        raise NotImplementedError('must be implemented by subclass')

    def num_children(self, p):
        """Return number of children of position p"""
        raise NotImplementedError('must be implemented by subclass')

    def children(self, p):
        """Return an iteration of all children of position p"""
        raise NotImplementedError('must be implemented by subclass')

    def __len__(self):
        """Return number of positions stored in tree"""
        raise NotImplementedError('must be implemented by subclass')

    # ----------methods implemented in this class
    def is_root(self, p):
        """Return True if position p is the same as the position of root"""
        return self.root() == p

    def is_leaf(self, p):
        """Return True if position p has no children"""
        return self.num_children(p) == 0

    def is_empty(self):
        """Return True if tree does not contain any positions"""
        return len(self) == 0
