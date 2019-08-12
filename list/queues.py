"""
FIFO : First-in, First-out
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