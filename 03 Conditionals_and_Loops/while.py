### The while Loop
#The `while` loop in Python repeatedly executes a block of code as long as a specified condition is `True`.


print("The while Loop:")
count = 0
while count < 5:  # Loop continues as long as count is less than 5
    print(count)
    count += 1  # Increment count by 1
# Output: 0 1 2 3 4

print("Loop ended\n")




### The Python break and continue Statements
    # - **break**: Exits the loop immediately.
    # - **continue**: Skips the rest of the current iteration and moves to the next iteration.

print("The break Statement:")
count = 0
while count < 5:
    if count == 3:
        break  # Exit the loop when count is 3
    print(count)
    count += 1
# Output: 0 1 2
print("Loop ended\n")


print("The continue Statement:")
count = 0
while count < 5:
    count += 1
    if count == 3:
        continue  # Skip the rest of the loop for count == 3
    print(count)
# Output: 1 2 4 5
print("Loop ended\n")




### The else Clause
# The `else` clause in a `while` loop executes if the loop completes normally (i.e., not interrupted by `break`).

print("The else Clause:")
count = 0
while count < 5:
    print(count)
    count += 1
else:
    print("Loop completed without break")
# Output: 0 1 2 3 4
# Output: Loop completed without break
print("Loop ended\n")

count = 0
while count < 5:
    if count == 3:
        break
    print(count)
    count += 1
else:
    print("Loop completed without break")
# Output: 0 1 2
print("Loop ended\n")




### Infinite Loops
# An infinite loop runs indefinitely because the condition is always `True`. Ensure there is a way to exit the loop, typically with a `break` statement.

print("Infinite Loop (with break):")
count = 0
while True:  # Infinite loop
    print(count)
    count += 1
    if count == 5:
        break  # Exit loop after count reaches 5
# Output: 0 1 2 3 4
print("Loop ended\n")





### Nested while Loops
# A nested `while` loop is a loop inside another `while` loop. Both loops will run according to their respective conditions.
print("Nested while Loops:")
outer_count = 0
while outer_count < 3:
    inner_count = 0
    while inner_count < 2:
        print(f"outer_count: {outer_count}, inner_count: {inner_count}")
        inner_count += 1
    outer_count += 1
# Output:
# outer_count: 0, inner_count: 0
# outer_count: 0, inner_count: 1
# outer_count: 1, inner_count: 0
# outer_count: 1, inner_count: 1
# outer_count: 2, inner_count: 0
# outer_count: 2, inner_count: 1
print("Loop ended\n")




### One-Line while Loops
# A `while` loop can be written in a single line if the loop body is simple.

print("One-Line while Loop:")
count = 0
while count < 5: print(count); count += 1
# Output: 0 1 2 3 4
print("Loop ended\n")


### Conclusion
# The `while` loop in Python is a powerful tool for executing code repeatedly based on a condition. It can be controlled and modified using `break`, `continue`, and `else` statements. Infinite loops should be used with caution and typically include a `break` statement to prevent them from running forever. Nested `while` loops allow for more complex iterations, and one-line `while` loops offer a concise syntax for simple loops.