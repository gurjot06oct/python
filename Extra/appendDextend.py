list_value = [1,2,3,4,5]
list_value_2 = list_value[:]
list_element = [6,7,8,9]

# Appending
list_value.append(list_element)
print(list_value) # [1, 2, 3, 4, 5, [6, 7, 8, 9]]
list_element.append(10)
print(list_value) # [1, 2, 3, 4, 5, [6, 7, 8, 9, 10]]


# Extending
list_value_2.extend(list_element)
print(list_value_2) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_element.append(11)
print(list_value_2) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
