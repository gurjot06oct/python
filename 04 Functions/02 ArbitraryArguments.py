def my_function(*args):
    print(type(args)) # tuple
    for arg in args:
        print(arg)

my_function(1, 2, 3)


def my_function(**kwargs):
    print(type(kwargs)) # dict
    for key, value in kwargs.items():
        print(key, ":", value)

my_function(name="Alice", age=30)
