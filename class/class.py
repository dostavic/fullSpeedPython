class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, mmy name is %s" % self.name)

a = Person("Peter", 20);
b = Person("Anna", 19)

a.greet()
b.greet()

print(a.name)
print(a.age)

print(b.name)
print(b.age)

class Rectange:
    def __init__(self, x1, y1, x2, y2):
        if x1 < x2 and y1 > y2:
            self.x1 = x1
            self.x2 = x2
            self.y1 = y1
            self.y2 = y2
        else:
            print("Incorrect coordinates of the rectange!")

    def width(self):
        return self.x2 - self.x1
    
    def height(self):
        return self.y1 - self.y2
    
    def area(self):
        return self.width() * self.height()
    
    def perimeter(self):
        return 2 * self.width() + 2 * self.height()
    
    def __str__(self):
        return f'{self.x1}, {self.y1}, {self.x2}, {self.y2}' 
    
    def __str__Rev(self):
        return(str(self.x1) + ', ' + str(self.y1) + ', ' + str(self.x2) + ', '+str(self.y2))

    def __repr__(self):
        return(str(self.x1) + ', ' + str(self.y1) + ', ' + str(self.x2) + ', '+str(self.y2))
    
r = Rectange(2, 7, 8, 4)
print(r.width())

print(r)