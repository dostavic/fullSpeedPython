for value in [0, 1, 2, 3, 4, 5]:
    print(value * value)

myList = [1, 5, 7]
sum = 0
for value in myList:
    sum = sum + value
print(sum)

for x in range(6):
    print(x)

myList = [1, 5, 7]
for i in range(len(myList)):
    print("Index:", i, "Value:", myList[i])

myList = [1, 5, 7]
for i, value in enumerate(myList):
    print("Index:", i, "Value:", value)

for x in "Full Speed Python":
    print(x)