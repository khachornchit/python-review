#1st method
sq1 = []
for x in range(10):
    sq1.append(x**2)

print("sq1 = ", sq1)

# 2nd method
sq2 = [x**2 for x in range(10)]
print("sq2 = ", sq2)

sq3 = [(x,y) for x in [1,2,3] for y in [3,1,4] if x!=y]
print("sq3 = ", sq3)

vec = [-4, -2, 0, 2, 4]
print("x*2", [x*2 for x in vec])

print("x if x>0", [x for x in vec if x>=0])

print("abs(x) = ", [abs(x) for x in vec])

freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print("weapon.strip() = ", [weapon.strip() for weapon in freshfruit])

print("(x, x**2) = ", [(x, x**2) for x in range(6)])

vec2 = [[1,2,3], [4,5,6], [7,8,9]]
print("num = ", [num for elem in vec2 for num in elem])