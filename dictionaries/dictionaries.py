from collections import OrderedDict

ages = {
    "Peter": 10,
    "Isabel": 11,
    "Anna": 9,
    "Thomas": 10,
    "Bob": 10,
    "Joseph": 11,
    "Maria": 12,
    "Gabriel": 10,
}

print("Get age of peter:")
print(ages["Peter"])

print("Get age of all persons")
for key, value in ages.items():
    print(key, value)


new_dict = dict()
new_dict = {}

ages = dict()
ages['Peter'] = 12
ages['Susan'] = 13
for key, value in ages.items():
    print(key, value)


ages = OrderedDict()

ages['Peter'] = 12
ages['Susan'] = 10
ages['Maria'] = 5

for key, value in ages.items():
    print(key, value)


d = {
    0: [0, 0, 0],
    1: [1, 1, 1],
    2: [2, 2, 2],
}

print(d[2])


ages = {
    "Peter": 10,
    "Isabel": 11,
    "Anna": 9,
    "Thomas": 10,
    "Bob": 10,
    "Joseph": 11,
    "Maria": 12,
    "Gabriel": 10,
}

for x in ages:
    print(x)

for x in ages:
    print(ages[x])

for x in ages.values():
    print(x)

for name, age in ages.items():
    print(name, age)