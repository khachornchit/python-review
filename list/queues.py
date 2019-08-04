"""
first-in, first-out FIFO
"""

from collections import deque
q = deque(["Eric", "John", "Michael"])
q.append("Terry")
q.append("Graham")
print("q original = ", q)

q.popleft()
print("q after pop = ", q)

q.popleft()
print("q after pop = ", q)