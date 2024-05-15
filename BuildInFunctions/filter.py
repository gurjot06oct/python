# filter(): Constructs an iterator from elements of an iterable for which a function returns true
filtered = filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5])
print(filtered) # <filter object at 0x789db7b237c0>
print(list(filtered))