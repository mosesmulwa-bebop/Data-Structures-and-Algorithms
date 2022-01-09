from BinaryEulerTour import BinaryEulerTour


class BinaryLayout(BinaryEulerTour):
    """Class for computing (x,y) coordinates for each node of a binary tree.

    The geometry is determined by an algorithm that assigns x- and y-coordinates to each
    position p of a binary tree T using the following two rules:
    • x(p) is the number of positions visited before p in an inorder traversal of T.
    • y(p) is the depth of p in T.
    """
    def __init__(self, tree):
        super().__init__(tree)                          # must call the parent constructor
        self. count = 0                                 # initialize count of processed nodes

    def _hook_invisit(self, p, d, path):
        p.element().setX(self. count)                   # x-coordinate serialized by count
        p.element().setY(d)                             # y-coordinate is depth
        self. count += 1                                # advance count of processed nodes
