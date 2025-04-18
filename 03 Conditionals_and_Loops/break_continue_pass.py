# Example of break
print("Example of break:")
for i in range(1, 10):
    if i == 5:
        break  # Exit the loop when i is 5
    print(i)
# The loop will terminate when i is 5, so the output will be:
# Output: 1 2 3 4
print("Loop ended\n")
# Output: Loop ended






# Example of continue
print("Example of continue:")
for i in range(1, 10):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)
# Even numbers will be skipped, so the output will be:
# Output: 1 3 5 7 9
print("Loop completed\n")
# Output: Loop completed







# Example of pass
print("Example of pass:")
for i in range(1, 10):
    if i % 2 == 0:
        pass  # Do nothing for even numbers
    else:
        print(i)
# pass does nothing, so the output will be the same as if the condition was not there.
# Output: 1 3 5 7 9
print("Loop completed\n")
# Output: Loop completed










# Combined example of break, continue, and pass
print("Combined example:")
for i in range(1, 10):
    if i == 5:
        break  # Exit the loop when i is 5
    elif i % 2 == 0:
        continue  # Skip the rest of the loop for even numbers
    else:
        pass  # Do nothing for odd numbers except printing
    print(i)
# The loop will break when i is 5, and even numbers will be skipped. So the output will be:
# Output: 1 3
print("Loop completed")
# Output: Loop completed
