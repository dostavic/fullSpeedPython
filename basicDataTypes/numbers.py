a = 2
print(type(a))

b = 2.5
print(type(b))

print(a + b)
print((a + b) * 2)
print(2 + 2 + 4 - 2 / 3)


def MathOp():
    a = 3 / 2
    b = 3 // 2
    c = 3 % 2
    d = 3 ** 2
    return [a, b, c, d]


list = [a, b, c, d] = MathOp()
for i in list:
    print(i)


def checkParity(n):
    if n % 2 == 0:
        return 0
    return 1


def checkParityRev(n):
    result = n % 2
    return result


print(checkParity(5))


def inRange(x, y):
    return x < 1 / 3 < y
