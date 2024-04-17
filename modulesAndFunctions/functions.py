import math


def do_hello():
    print("Hello")
    print("World")
do_hello()

def add_one(val):
    print("Function got value", val + 1)
add_one(1)

def add_one2(val):
    print("Function got value", val)
    return val + 1
value = add_one2(1)
print(value)

def findGCD(a, b):
    return math.gcd(a, b)

def calculateSinCosTan(x):
    return [math.sin(x), math.cos(x), math.tan(x)]

def findMaximum(x, y):
    return max(x, y)

def isDivisible(x, y):
    return x % y == 0