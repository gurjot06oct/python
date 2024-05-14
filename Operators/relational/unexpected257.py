# Python caches integers in the range [-5, 256], so integers in that range are usually but not always identical.

# What you see for 257 is the Python compiler optimizing identical literals when compiled in the same code object.

# When typing in the Python shell each line is a completely different statement, parsed and compiled separately, thus:

# >>> a = 257
# >>> b = 257
# >>> a is b
# 


# But if you put the same code into a file:

#   a = 257
#   b = 257
#   print( a is b)
#   Output : True
# This happens whenever the compiler has a chance to analyze the literals together