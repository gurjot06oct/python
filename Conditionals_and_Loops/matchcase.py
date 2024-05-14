# Case conditions can only evaluate numeric, iterables, None
# When evaluating iterables, only the order of values is considered, while the type of iterable is ignored.
# It's important to note that sets cannot be used in case conditions; they are an exception to this rule.


# Define a variable 'e' by evaluating user input
e = eval(input("Enter anything: "))

# Use a match statement to evaluate 'e' against different cases
match e:
    # Check if 'e' is an iterable containing elements 1, 2, and 3 in any order
    # `List` is printed for both list and tuple input
    case [1, 2, 3]:
        print('List')  # If matched, print 'List'
    
    case (1, 2, 3):
        print('Tuple')  # If matched, print 'Tuple'


    # Check if 'e' is None
    case None:
        print('None')  # If matched, print 'None'
    
    # Check if 'e' is a iterable with any key-value pair
    case {"a": "1323234"}:
        print("Dictionary")  # If matched, print 'Dictionary'
    
    # Check if 'e' evaluates to True
    case bool(1):
        print('Boolean')  # If matched, print 'Boolean'
    
    # Sets cannot be used in case conditions
    # case {1,2,3}:
    #     print("Set")

    # Default case if none of the above matches
    case _:
        print('None')  # If no case matches, print 'None'
