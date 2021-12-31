from ArrayStack import ArrayStack

S = ArrayStack()
S.push(5)
S.push(3)
print(len(S))
print(S.pop())
S.pop()
print(S.is_empty())
