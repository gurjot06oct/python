def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()


# Iterate over gen
for value in gen:
    print(value)

# Won't work as already iterated
for value in gen:
    print(value)
