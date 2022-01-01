from ArrayDeque import ArrayDeque


D = ArrayDeque()
D.add_last(5)
D.add_last(3)
D.add_last(7)
print(str(D))
print(D.first())
print(D.last())
D.delete_last()
print(len(D))
D.add_first(76)
print(str(D))
D.delete_first()
print(str(D))
