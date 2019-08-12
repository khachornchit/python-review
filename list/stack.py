"""
LIFO : Last-in, First-out
"""

stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print("stack original ", stack)

stack.pop()
print("stack after stack.pop()", stack)

stack.pop()
print("stack after stack.pop()", stack)