def multiply(*args):
    print(args)
    x = 2
    for arg in args:
        x += arg * 2

    return x


print(multiply(1, 2, 3))