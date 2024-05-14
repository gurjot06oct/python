# Creating an empty set
my_set = set({})

# Create a set
my_set = {1, 2, 3, 4, 5}
print(my_set)



# Accessing the elements
# By for loop
for i in my_set:
    print(i)
# By unpacking
print(*my_set)



# add(): Adds an element to the set
my_set.add(6)
print("add():", my_set)  # Output: {1, 2, 3, 4, 5, 6}


# clear(): Removes all the elements from the set
my_set.clear()
print("clear():", my_set)  # Output: set()


# copy(): Returns a copy of the set
original_set = {1, 2, 3}
copied_set = original_set.copy()
print("copy():", copied_set)  # Output: {1, 2, 3}


# difference(): Returns a set containing the difference between two sets
other_set = {3, 4, 5}
difference_set = original_set.difference(other_set)
print("difference():", difference_set)  # Output: {1, 2}


# difference_update(): Removes the items in this set that are also included in another specified set
original_set.difference_update(other_set)
print("difference_update():", original_set)  # Output: {1, 2}


# discard(): Removes the specified item
original_set.discard(1)
print("discard():", original_set)  # Output: {2}


# intersection(): Returns a set that is the intersection of two other sets
intersection_set = original_set.intersection(other_set)
print("intersection():", intersection_set)  # Output: set()


# intersection_update(): Removes the items in this set that are not present in other specified set(s)
original_set.intersection_update(other_set)
print("intersection_update():", original_set)  # Output: set()


# isdisjoint(): Returns whether two sets have an intersection or not
are_disjoint = original_set.isdisjoint(other_set)
print("isdisjoint():", are_disjoint)  # Output: True


# issubset(): Returns whether another set contains this set or not
is_subset = original_set.issubset(other_set)
print("issubset():", is_subset)  # Output: True


# issuperset(): Returns whether this set contains another set or not
is_superset = original_set.issuperset(other_set)
print("issuperset():", is_superset)  # Output: False


# pop() -> val: Removes an element from the set
popped_element = copied_set.pop()
print("pop():", popped_element)  # Output: 1


# remove() -> None: Removes the specified element
copied_set.remove(3)
print("remove():", copied_set)  # Output: {2}


# symmetric_difference(): Returns a set with the symmetric differences of two sets - Delta
print(original_set, other_set)
symmetric_difference_set = original_set.symmetric_difference(other_set)
print("symmetric_difference():", symmetric_difference_set)  # Output: {3, 4, 5}


# symmetric_difference_update(): Inserts the symmetric differences from this set and another
original_set.symmetric_difference_update(other_set)
print("symmetric_difference_update():", original_set)  # Output: {3, 4, 5}


# union(): Return a set containing the union of sets
union_set = original_set.union(other_set)
print("union():", union_set)  # Output: {3, 4, 5}


# update(): Update the set with the union of this set and others
original_set.update(other_set)
print("update():", original_set)  # Output: {3, 4, 5}
