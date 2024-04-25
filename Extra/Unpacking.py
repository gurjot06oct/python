my_list = [1, 2, 3,4]
a, b, *c = my_list


my_tuple = (4, 5, 6)
x, y, z = my_tuple


my_string = "abc"
p, q, r = my_string


my_dict = {'a': 1, 'b': 2, 'c': 3}
x, y, z = my_dict # keys

my_dict = {'a': 1, 'b': 2, 'c': 3}
x, y, z = my_dict.items()  # Unpack key-value pairs
x, y, z = my_dict.values()  # Unpack values


my_set = {1, 2, 3}
x, y, z = my_set  # Order may vary


# -----  advanced -------
my_string = "Fetching only first three"
p, q, r,*s = my_string
# p,q,r have first three letters
# *s has remaining string as list


my_string = "first and last only"
a,*b,c = my_string