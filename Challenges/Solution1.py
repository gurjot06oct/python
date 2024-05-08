def mystery_function(x):
    print(x)
    # do something else
    # It can return anything true, false, none, etc.
    return True

active_list = [1, 2, 3, 4, 5, 6, 7]
active_list_2 = [(mystery_function(i) or True) and i for i in active_list]
print(active_list_2)