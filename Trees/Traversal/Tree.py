from LinkedLists.Singly.LinkedQueue import LinkedQueue


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

    def depth(self, p):
        """Return the number of levels separating position p from the root"""
        if p == self.root():
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def _height_of_position_p(self, p):
        """Return the height of the subtree rooted at position p"""
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height_of_position_p(c) for c in self.children(p))

    def height(self, p=None):
        """Return the height of the subtree rooted at position p"""
        if p is None:
            p = self.root()
        return self._height_of_position_p(p)

    def __iter__(self):
        """Returns an iteration of all elements in tree"""
        for p in self.positions:
            yield p.element()

    def positions(self):
        """Return an iteration of all positions in tree"""
        return self.preorder()

    # ----------------------------Traversal---------------------------------------
    def preorder(self):
        """Return an iteration of all positions in tree using preorder traversal"""

        if not self.is_empty():
            for p in self._preorder_subtree(self.root()):
                yield p

    def _preorder_subtree(self, p):
        """Return an iteration of all positions in subtree rooted at p using preorder traversal"""
        yield p                                             # perform visit action
        for c in self.children(p):                          # loop over all children
            for other in self._preorder_subtree(c):         # get subtree of each child
                yield other                                 # yield to our caller

    def postorder(self):
        """Return an iteration of all positions in tree using postorder traversal"""

        if not self.is_empty():
            for p in self._postorder_subtree(self.root()):
                yield p

    def _postorder_subtree(self, p):
        """Return an iteration of all positions in subtree rooted at p using postorder traversal"""

        for c in self.children(p):                          # loop over all children
            for other in self._preorder_subtree(c):         # get subtree of each child
                yield other                                 # yield to our caller
        yield p                                             # perform visit action

    def breadth_first(self):
        """Generate an iteration of all positions using breadth_first traversal"""
        if not self.is_empty():
            fringe = LinkedQueue()                          # known positions not yet yielded
            fringe.enqueue(self.root())                     # starting with the root
            while not fringe.is_empty:
                p = fringe.dequeue()                        # remove from front of queue
                yield p
                for child in self.children(p):
                    fringe.enqueue(child)                   # add children to the back of the queue



