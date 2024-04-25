# same for <,<=,>,>=
# Set vs Set 
print({1, 2} < {1, 2, 3})
print({1, 2,3,4} > {1, 2, 3})
print({1, 2, 3} <= {1, 2, 3})
print({1, 2, 3} >= {1, 2, 3})
print({1,2,3} & {2,3,4}) # a&b (intersection)
print({1,2,3} | {2,3,4}) # a|b (union)
print({1,2,3} ^ {2,3,4}) # a|b - a&b (delta)

# Frozenset vs Frozenset
result_ff = frozenset({1, 2}) < frozenset({1, 2, 3})
