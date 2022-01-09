from ExpressionTree import ExpressionTree


def build_expression_tree(expression):
    """ The algorithm uses a stack S while scanning tokens of the input expression E to
        find values, operators, and right parentheses. (Left parentheses are ignored.)
        • When we see an operator ◦, we push that string on the stack.
        • When we see a literal value v, we create a single-node expression tree T
          storing v, and push T on the stack.
        • When we see a right parenthesis, ')', we pop the top three items from the
          stack S, which represent a subexpression (E1 ◦ E2). We then construct a
          tree T using trees for E1 and E2 as subtrees of the root storing ◦, and push
          the resulting tree T back on the stack."""
    s = []                                                           # use list as stack

    for token in expression:
        if token == '(':
            continue
        elif token in '+-/x*':
            s.append(token)
        elif token != '(' and token not in '+-/x' and token != ')':          # literal
            T = ExpressionTree(token)
            s.append(T)
        elif token == ')':                                          # pop top three items
            E1 = s.pop()
            operator = s.pop()
            E2 = s.pop()
            T = ExpressionTree(operator, E1, E2)
            s.append(T)

    return s.pop()

