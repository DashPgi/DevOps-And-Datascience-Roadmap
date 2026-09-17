# Args
def multiply(*args):
    print(args)
    x = 1
    for arg in args:
        x *= arg
    return x

def plus(*args):
    x= 1
    for arg in args:
        x += arg
    return x
def minus(*args):
    x= 1
    for arg in args:
        x -= arg
    return x
def divide(*args):
    x= 1
    for arg in args:
        x /= arg
    return x


def apply(*args,operator):
    if operator == '+':
        return multiply(*args)
    elif operator == '*':
        return plus(*args)
    elif operator == '/':
        return divide(*args)
    elif operator == '-':
        return minus(*args)
    else:
        raise ValueError('Invalid operator')

operator = str(input('Please enter operator: +, *, /, -: '))
print(apply(1, 2, 3, operator=operator))

# key args

def named(**kwargs):
    print(kwargs)

dict = {"name" : "parsa","age":25}

named(**dict)

# Type Hinting

from typing import List
def list_avg(data : List)  -> float:
    return sum(list) / len(list)

data = 123
list_avg(data)