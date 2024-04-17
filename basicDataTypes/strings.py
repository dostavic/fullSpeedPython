hi = "hello"
print(hi)

bye = 'goodbye'
print(bye)


hi = "hello"
hi += "world"
print(hi)

# hi = "hello"
# hi += 4
# print(hi)

print("Hello" * 3)


def getStr(s):
    sNew = ""
    for i in range(0, len(s)):
        sNew += s[i] * 3
    return [sNew, len(sNew)]

def findOccurence(s):
    return [s.index("b"), s.index("ccc")]

def findOccurenceRev(s):
    return [s.find("b"), s.find("ccc")]

print(findOccurence("aaabbbccc"))

def changeCase(s):
    return [s.upper(), s.lower()]