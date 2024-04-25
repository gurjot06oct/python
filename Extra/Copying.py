# Shallow and Deep Copy
import copy

# -------copy library------
l = [0, 1, [2, 3]]
l_shallow_copy = l.copy()
l_deepcopy = copy.deepcopy(l)
l[1] = 100
l[2][0] = 200
print(l) # [0, 100, [200, 3]]
print(l_shallow_copy) # [0, 1, [200, 3]]
print(l_deepcopy) # [0, 1, [2, 3]]


#------ slicing -------
l = [0, 1, [2, 3]]
l_slice_shallow_copy = l[:]
l_slice_deepcopy = copy.deepcopy(l[:])
l[1] = 100
l[2][0] = 200
print(l) # [0, 100, [200, 3]]
print(l_slice_shallow_copy) # [0, 1, [200, 3]]
print(l_slice_deepcopy) # [0, 1, [2, 3]]