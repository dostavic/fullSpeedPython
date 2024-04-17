students = {
    "Peter": {"age": 10, "address": "Lisbon"},
    "Isabel": {"age": 11, "address": "Sesimbra"},
    "Anna": {"age": 9, "address": "Lisbon"},
}
# print(students)
# print(students["Peter"])
# print(students["Peter"]["address"])
#
#
# for p_id, p_info in students.items():
#     print("\nPerson Name:", p_id)
#     for key in p_info:
#         print(key + ":", p_info[key])


def lengthDictionary(Students):
    return len(Students)


def calculateAvg(ages):
    s = 0
    for key, value in ages.items():
        s += value
    return s / len(ages)


def calculateAvgRev(ages):
    length=len(ages)
    return(sum(ages.values())/length)


def oldestStudent(ages):
    maxAge = max(ages.values())
    for key, value in ages.items():
        if value == maxAge:
            return key

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

print(oldestStudent(ages))


def oldestStudentRev(ages):
    value = list(ages.values())
    key = list(ages.keys())
    return key[value.index(max(value))]


def updateAges(ages, n):
    for key in ages:
        ages[key] += n
    return ages


def totalStudents(students):
    return len(students)


def calculateAverageAge(students):
    return sum(student['age'] for student in students.values()) / len(students)


calculateAverageAge(students)


def calculateAverageAgeRev(students):
    add_age = 0
    for thing in students.values():
        age = thing['age']
        add_age = add_age + age

    return (add_age / len(students.keys()))


def find_students(address, students):
    return sorted([name for name, info in students.items() if info['address'] == address])

print(find_students("Lisbon", students))