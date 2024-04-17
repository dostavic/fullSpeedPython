n = 10
while n > 0:
    print(n)
    n -= 1

def sumList(l):
    s = 0
    for val in l:
        s += val
    return s

def findMaximum(list):
    max = list[0]
    for val in list:
        if val > max:
            max = val
    return max

def findMaximumValueIndex(list):
    max = list[0]
    index = 0
    # for i, value in enumerate(list):
    for i in range(len(list)):
        if list[i] > max:
            max = list[i]
            index = i
    return [index, max]

def reverse(list):
    listNew = []
    for i in range(len(list) - 1, -1, -1):
        listNew.append(list[i])
    return listNew

def reverseRev(list):
    length = len(list)
    s = length

    new_list = [None]*length

    for item in list:
        s = s - 1
        new_list[s] = item
    return new_list

def isSorted(list):
    for i, value in enumerate(list):
        if i > 0 and list[i] < list[i - 1]:
            return False
    return True

def hasDuplicates(list):
    for i, value in enumerate(list):
        for j in range(i + 1, len(list)):
            if list[i] == list[j]:
                return True
    return False