def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()
print(next(gen))
print(next(gen))
print(next(gen))
# print(next(gen)) # Error StopIteration, because all items have been iterated

gen2=my_generator()
# Iterate over gen
for value in gen2:
    print(value)

# Won't work as already iterated
for value in gen2:
    print(value)
