from EulerTour import EulerTour


class BinaryEulerTour(EulerTour):
    """Abstract base class for performing Euler tour of a binary tree.
    This version includes an additional hook invisit that is called after the tour
    of the left subtree (if any), yet before the tour of the right subtree (if any).

    Note: Right child is always assigned index 1 in path, even if no left sibling.
    """
    def tour(self, p, d, path):
        results = [None, None]                              # will update with results of recursions
        self._hook_previsit(p, d, path)                     # "pre visit” for p
        if self. tree.left(p) is not None:                  # consider left child
            path.append(0)
            results[0] = self. tour(self. tree.left(p), d+1, path)
            path.pop()
        self._hook_invisit(p, d, path)                      # "in visit” for p
        if self._tree.right(p) is not None:                 # consider right child
            path.append(1)
            results[1] = self. tour(self. tree.right(p), d+1, path)
            path.pop()
        answer = self._hook_postvisit(p, d, path, results)  # "post visit” p
        return answer

    def hook_invisit(self, p, d, path):
        pass                                                # can be overridden