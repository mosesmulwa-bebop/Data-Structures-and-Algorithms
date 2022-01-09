from LinkedBinaryTree import LinkedBinaryTree


class ExpressionTree(LinkedBinaryTree):
    """An arithmetic expression tree"""

    def __init__(self, token, left=None, right=None):
        """
        Create an expression tree.

        In a single parameter form, token should be a leaf value (e.g.,'42'),
        and the expression tree will have that value at an isolated node.

        In a three-parameter version, token should be an operator,
        and left and right should be existing ExpressionTree instances
        that become the operands for the binary operator.
        """

        super().__init__()                                  # Linked Binary Tree initialization
        if not isinstance(token, str):
            raise TypeError('Token should be a string')
        self._add_root(token)                               # use inherited non public method
        if left is not None:                                # presumably three parameter form
            if token not in '+-*/':
                raise ValueError('Token must be a valid parameter')
            self._attach(self.root(), left, right)

    def __str__(self):
        """Return string representation of expression"""
        pieces = []                                         # sequence of piecewise strings to compose
        self._parenthesize_recur(self.root(), pieces)
        return ''.join(pieces)

    def _parenthesize_recur(self, p, result):
        """Append piecewise representation of p's subtree to resulting list"""
        if self.is_leaf(p):
            result.append(str(p.element()))                     # leaf value as a string
        else:                                                   # it has children
            result.append('(')                                  # opening parenthesis
            self._parenthesize_recur(self.left(p), result)      # left subtree
            result.append(p.element())                          # operator
            self._parenthesize_recur(self.right(p), result)     # right subtree
            result.append(')')                                  # closing parenthesis

    def evaluate(self):
        """Return numeric result of the expression"""
        return self._evaluate_recur(self.root())

    def _evaluate_recur(self, p):
        """Return numeric result of the subtree rooted at p"""
        if self.is_leaf(p):                                   # if no children, just a number
            return p.element()
        else:                                                 # operator as center operating on left and right
            operator = p.element()                            # operator stored as string
            x = self._evaluate_recur(self.left(p))
            y = self._evaluate_recur(self.right(p))

            if operator == '+':
                return x + y
            elif operator == '-':
                return x - y
            elif operator == '-':
                return x - y
            else:
                return x * y



