from Tree import Tree


class BinaryTree(Tree):
    """Abstract base class representing a binary Tree structure"""

    # --------Additional abstract methods ----------------------------------
    def left(self, p):
        """Return the position of the left child of position p
        or None if there is no left child"""
        return NotImplementedError('must be implemented by the subclass')

    def right(self, p):
        """Return the position of the right child of position p
                or None if there is no right child"""
        return NotImplementedError('must be implemented by the subclass')

    # ---------Methods implemented in this class ------------------------
    def sibling(self, p):
        """Return position of p's sibling or None"""
        parent = self.parent(p)                         # get parent of p
        if parent is None:                              # p is the root
            return None                                 # has no sibling
        if p == self.left(parent):                    # if we are currently on the left
            return self.right(parent)                   # return right as sibling ,possibly none
        else:
            return self.left(parent)

    def children(self, p):
        """Return an iteration of Positions representing p's children"""
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

