def method1():
    return [x ** 2 for x in range(10)]


def method2():
    return [x ** 2 for x in range(10)]


def method3():
    return [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]


def method4(vec):
    return [x * 2 for x in vec]


def method5(vec):
    return [x for x in vec if x >= 0]


def method6(vec):
    return [abs(x) for x in vec]


def method7(freshfruit):
    return [weapon.strip() for weapon in freshfruit]


def method8():
    return [(x, x ** 2) for x in range(6)]


def method9(vec2):
    return [num for elem in vec2 for num in elem]


if __name__ == "__main__":
    # 1st method
    sq1 = method1()
    print("sq1 =", sq1)

    # 2nd method
    sq2 = method2()
    print("sq2 =", sq2)

    sq3 = method3()
    print("sq3 =", sq3)

    vec = [-4, -2, 0, 2, 4]
    print("x*2", method4(vec))
    print("x if x>0", method5(vec))
    print("abs(x) =", method6(vec))

    fresh_fruit = ['  banana', '  loganberry ', 'passion fruit  ']
    print("weapon.strip() =", method7(fresh_fruit))

    print("(x, x**2) =", method8())

    vec2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("num =", method9(vec2))
