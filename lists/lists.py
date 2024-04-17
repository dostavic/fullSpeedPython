l = [1, 2, 3, 4, 5]

l = [1, 2, 3, 4, 5]
print(l)
print(l[0])
print(l[1])


l = [1, 2, 3, 4, 5]
l1 = l[0:3]
l1 = l[3:5]

l = ['a', 'b', 'c', 'd', 'e']
print(l[0:3])


print([1, 2] + [3, 4])


l = [1, 2, 4, 8, 10]
for val in l:
    print(val)


def getSubList():
    l = [1, 4, 9, 10, 23]
    l1 = l[0:3]
    l2 = l[3:5]
    return [l1, l2]

def AppendtoList():
    l = [1, 4, 9, 10, 23]
    return l + [90]

def AppendtoListRev():
    l = [1, 4, 9, 10, 23]
    return l.append(90)

def getAverage():
    l1 = [1, 4, 9, 10, 23]
    return sum(l1) / len(l1)

def removeList():
    l1 = [1, 4, 9, 10, 23]
    l2 = [4, 9]
    l1.remove(4)
    l1.remove(9)
    return l1