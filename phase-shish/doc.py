# Args
def multiply(*args):
    print(args)
    x = 1
    for arg in args:
        x *= arg
    return x


def plus(*args):
    x = 1
    for arg in args:
        x += arg
    return x


def minus(*args):
    x = 1
    for arg in args:
        x -= arg
    return x


def divide(*args):
    x = 1
    for arg in args:
        x /= arg
    return x


def apply(*args, operator):
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


dict = {"name": "parsa", "age": 25}

named(**dict)

# Type Hinting

from typing import List


def list_avg(data: List) -> float:
    return sum(list) / len(list)


data = 123
list_avg(data)


# Custom error classes
class TooManyPagesReadError(ValueError):
    pass


class Book:
    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count
        self.page_read = 0

    def __repr__(self):
        return f"Book({self.name}, {self.page_count}, {self.page_read})"

    def read(self, pages: int):
        if self.page_read + pages > self.page_count:
            raise TooManyPagesReadError(
                f"You tried to read {self.page_read + pages} pages, but you only have {self.page_count} pages."
            )
        self.page_read += pages
        print(self.page_read)


python101 = Book("Python", 50)

try:
    python101.read(66)
    python101.read(60)
except TooManyPagesReadError as e:
    print(e)

    # Decorators

    users = {"usrname": "aria", "access_lvl": "admin"}


    def get_admin_password():
        return "1234"


    def make_secure(func):
        def secure_function():
            if users["access_lvl"] == "admin":
                return func()
            else:
                "no admin permissions"

        return secure_function


    get_admin_password = make_secure(get_admin_password)

    print(get_admin_password())
