# Basic BoilerPlate
# lambda a,b,c,d..: expression_to_return

# Lambda function to add two numbers
add = lambda x, y: x + y
print(add(3, 5))  # Output: 8
print(add)  # Output: <function <lambda> at 0x7f7bd1398540>
print(type(add))  # Output: <class 'function'>


# Sorting a list of tuples based on the second element using lambda function
data = [(1, 2), (4, 1), (3, 3)]
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)  # Output: [(4, 1), (1, 2), (3, 3)]



# Filtering a list of numbers to get only even numbers using lambda function
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6]
