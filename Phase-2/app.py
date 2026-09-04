var = "hello world"
print(var)
A = 10
B = 5

if A > B:
    print("A is greater than B")
elif A < B:
    print("A is less than B")
else:
    print("A is equal to B")

for i in range(B,A,2):
    if(i % 2 != 0):
        continue
    else:
     print(i)

match A:
    case 1:
        print("A = 1")
    case 2:
        print("A = 2")
    case 5:
        print("A = B")
    case 7:
        print("A = 7")
    case 8:
        print("A = 8")
    case 10:
        print("A = 10")

while( B == A ):
    B += 1
    print(B)

Input = int(input())

List = [1,2,3,4,5]
print(List)
Dictionary = {"first" : 1,"second" : 2,"third" : 3,"four" : 4,"five" : 5}
print(Dictionary)
Tuple = (1,2,3,4,5)
print(Tuple)
Set = {1,2,3,4,5}
print(Set)

def Withoutoutput():
    print("Hello World")
def Withinput(Input):
    return Input * 10

if Input <= 5:
    Withoutoutput()
else :
    Withinput(Input)


class Shape(ABC):
    def ELEMENT(self, metal):
        self.metal = metal

    def area(self):
        pass

    def perimeter(self):
        pass

    def volume(self):
        pass


class Color:
    red = "red"
    green = "green"
    blue = "blue"
    white = "white"
    black = "black"
    class codecolor(Enum):
        RED = "FF0000"
        GREEN = "00FF40"
        BLUE = "0004FF"

    def __init__(self, color):
        self.color = color

    def __len__(self):
        return len(self.color)


class Rectangle(Shape, Color):
    shape = "rectangle"
    Color = Color.red

    def __call__(self):
        return "This Class Isn't Class Anyway"

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def area(self):
        return self.x * self.y

    def perimeter(self):
        return (self.x + self.y) * 2

    def volume(self):
        return self.x * self.y * self.z

    @property
    def Persianname(self):
        return "Moraba"


class Square(Shape):
    shape = "square"

    def __str__(self):
        return "This Square have an area and Perimetr and also Volume"

    def __repr__(self):
        return f"This Square have jus one width : {self.x}"

    def __init__(self, x):
        self.x = x

    def area(self):
        return self.x ** 2

    def perimeter(self):
        return self.x * 4

    def volume(self):
        return self.x * self.x * self.x

    @staticmethod
    def info():
        print("This Is a Square")


class Triangle(Shape, Color):
    shape = "triangle"  # public
    _shape = "have a 3 different line"  # protected (need object to show itself)
    __shape = "it is 2D shape"  # private(need a method to show itself)

    def __init__(self, a, b, c, metal):
        super().ELEMENT(metal)
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    @classmethod
    def equal_sides(cls, side):
        return cls(side, side, side, Color.white)


C = Color(["red", "green", "blue", "white", "black"])
R = Rectangle(1, 2, 3)
S = Square(4)
T = Triangle(1, 2, 3, "metalic")
t = Triangle.equal_sides(5)


print(R.area(), R.perimeter(), R.volume(), R.Color)
print(S.area())
print(t.perimeter())
print(T.metal)
print(S)
print(repr(S))
print(len(C))
print(R())
print(R.Persianname)

def numbers(max_num):
    num = 1
    while num <= max_num:
        yield num
        num += 1

for i in numbers(5):
    print(i)

class MyNumbers:
    def __init__(self, max_num):
        self.num = 1
        self.max_num = max_num

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= self.max_num:
            x = self.num
            self.num += 1
            return x
        raise StopIteration

numbers = MyNumbers(5)

for i in numbers:
    print(i)

file = open("test.txt", "w")
file.write("Hello\n")
file.write("Python\n")
file.close()

file = open("test.txt", "r")
text = file.read()
print(text)
file.close()

file = open("test.txt", "a")
file.write("New line\n")
file.close()

file = open("test.txt", "r")
print(file.readline())
print(file.readlines())
file.close()

with open("test.txt", "r") as file:
    print(file.read())

with open("test.txt", "w") as file:
    file.write("New text")

with open("test.txt", "a") as file:
    file.write("\nAnother text")