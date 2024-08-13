my_list = [1, 2, 3, 4, 5]
my_list = list((1, 2, 3, 4, 5))
my_list = [x for x in range(1, 6)]



# access these elements
my_list = [10, 20, 30, 40, 50]
first_element = my_list[0]  # Access the first element
third_element = my_list[2]  # Access the third element
last_element = my_list[-1]  # Access the last element
print(my_list[-3:-1])  # Output: [30, 40]
my_list = [10, 20, 30, 40, 50]
for element in my_list:
    print(element)




# List Comprehension

# Basic List Comprehension
squares = [x**2 for x in range(10)]
print("Basic List Comprehension:", squares)


# List Comprehension with Conditionals
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print("List Comprehension with Conditionals:", even_squares)


# Nested List Comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print("Nested List Comprehension:", flattened)


# List Comprehension with Multiple Input Iterables
pairs = [(x, y) for x in range(3) for y in range(3)]
print("List Comprehension with Multiple Input Iterables:", pairs)


# List Comprehension with Nested Conditionals
even_greater_than_5 = [x for x in range(10) if x % 2 == 0 if x > 5]
print("List Comprehension with Nested Conditionals:", even_greater_than_5)


# List Comprehension with Expressions
doubled = [x * 2 for x in range(10)]
print("List Comprehension with Expressions:", doubled)


# List Comprehension with if-else
parity = ['even' if x % 2 == 0 else 'odd' for x in range(10)]
print("List Comprehension with if-else:", parity)


# Nested List Comprehension with if-else
processed_matrix = [[x*2 if x % 2 == 0 else x for x in row] for row in matrix]
print("Nested List Comprehension with if-else:", processed_matrix)




# Copy a list
my_list2 = my_list.copy()
print(my_list2)



# Methods
# Initialize a list
my_list = [1, 2, 3, 4, 5]



# append(): Adds an element at the end of the list
my_list.append(6)
print("append():", my_list)  # Output: [1, 2, 3, 4, 5, 6]



# clear(): Removes all the elements from the list
my_list.clear()
print("clear():", my_list)  # Output: []



# copy(): Returns a copy of the list
original_list = [1, 2, 3]
copied_list = original_list.copy()
print("copy():", copied_list)  # Output: [1, 2, 3]


# count(): Returns the number of elements with the specified value
count_of_2 = original_list.count(2)
print("count():", count_of_2)  # Output: 1


# extend(): Add the elements of a list (or any iterable), to the end of the current list
original_list.extend([4, 5, 6])
print("extend():", original_list)  # Output: [1, 2, 3, 4, 5, 6]


# index(): Returns the index of the first element with the specified value
index_of_3 = original_list.index(3)
print("index():", index_of_3)  # Output: 2


# insert(): Adds an element at the specified position
original_list.insert(2, 2.5)
print("insert():", original_list)  # Output: [1, 2, 2.5, 3, 4, 5, 6]


# pop(index=-1): Removes the element at the specified position
popped_element = original_list.pop(2)
print("pop():", popped_element)  # Output: 2.5


# remove(): Removes the item with the specified value
original_list.remove(3)
print("remove():", original_list)  # Output: [1, 2, 4, 5, 6]


# reverse(): Reverses the order of the list
original_list.reverse()
print("reverse():", original_list)  # Output: [6, 5, 4, 2, 1]


# sort(): Sorts the list
original_list.sort()
print("sort():", original_list)  # Output: [1, 2, 4, 5, 6]

another_list = [-1, -3, -5, 2, 4, 6]
another_list.sort(key=lambda x: x * x)
print(another_list)  # Output: [-1, 2, -3, 4, -5, 6]
another_list.sort(reverse=True)
print(another_list)  # Output: [6, 4, 2, -1, -3, -5]