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
