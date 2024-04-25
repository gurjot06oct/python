# accessing after assigning

# Using walrus operator in a while loop
x = 0
while (x := x + 1) < 10:
    print(x)

# Using walrus operator in list comprehension
values = [x for i in range(5) if (x := i * 2) > 4]
print(values)

# Using walrus operator in conditional expression
data = [10, 20, 30]
if (length := len(data)) > 2:
    print(f"List is long ({length} elements)")
