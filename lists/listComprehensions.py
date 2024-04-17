print([x * x for x in [0, 1, 2, 3]])

range(4)

print([x * x for x in range(4)])

print([x for x in range(10) if x % 2 == 0])

def getSquare():
    return [x * x for x in range(1, 11)]

def getCube():
    return [x * x * x for x in range(1, 21)]

def getCubeRev():
    return [x ** 3 for x in range(1,21)]

def ListofEvenOdds():
    return [
        [x for x in range(0, 21) if x % 2 == 0],
        [x for x in range(0, 21) if x % 2 != 0]
    ]

def ListofEvenOddsRev():
    l1 = [x for x in range(0, 21) if x % 2 == 0],
    return [
        l1,
        [x for x in range(0, 21) if (x not in l1)]
    ]

def evenSquareSum():
    return sum([x * x for x in range(1, 21) if x % 2 == 0])

def evenSquareSumRev():
    even = [x * x for x in range(0, 21, 2)]
    return sum(even)

def getSquare2():
    return [x * x for x in range(0, 21, 2) if x % 3 != 0]