class EulerTour:
    """Abstract base class for defining an euler tour of a tree

    _hook_previsit and _hook_postvisit may be overridden by subclasses
    """

    def __init__(self, tree):
        self._tree = tree

    def tree(self):
        """Return reference to tree being traversed"""
        return self._tree

    def execute(self):
        """Perform the tour and return any result from the post visit of root"""
        if len(self._tree) > 0:
            return self._tour(self._tree.root(), 0, [])               # start the recursion

    def _tour(self, p, d, path):
        """Perform a tour of the subtree rooted at p

        p    - position of root
        d    - depth of position p
        path - list of indices  of children on path from root to p
        """

        self._hook_previsit(p, d, path)                             # pre vist p
        results = []

        path.append(0)                                              # add new index to end of path before recursion
        for child in self._tree.children():
            results.append(self._tour(child, d+1, path))            # recur on child's surface
            path[-1] += 1                                           # increment index
        path.pop()                                                  # remove extraneous index from end of path

        answer = self._hook_postvisit(p, d, path, results)          # post visit p
        return answer

    def _hook_previsit(self, p, d, path):                           # can be overridden
        pass

    def _hook_postvisit(self, p, d, path, results):                 # can be overridden
        pass
