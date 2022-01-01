from ArrayQueue import ArrayQueue


Q = ArrayQueue()
print(str(Q))
Q.enqueue(5)
print(str(Q))
Q.enqueue(3)
print(str(Q))
print(len(Q))
Q.dequeue()
print(str(Q))

print(Q.first())
print(len(Q))
Q.dequeue()
print(Q.is_empty())
