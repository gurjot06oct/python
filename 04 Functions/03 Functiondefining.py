# -----Position only-------
def positional_only(x, y, /):
    print("Positional-only parameters:", x, y)

positional_only(1, 2)               # Valid: Positional arguments
# positional_only(x=1, y=2)           # Invalid: Cannot use keyword arguments
# positional_only(1, y=2)             # Invalid: Cannot use keyword arguments for x


#-------Keyword only------
def keyword_only(*, x, y):
    print("Keyword-only parameters:", x, y)

keyword_only(x=1, y=2)              # Valid: Keyword arguments
# keyword_only(1, 2)                  # Invalid: Must use keyword arguments


#-------position and keyword--------
def position_keyword(a, b,*, c=None):
    return a + b
print(position_keyword(1,b=2))
print(position_keyword(1,2))


# -------Mixed parameter-------
def mixed_parameters(x, /, *, y,z):
    print("Positional-only and keyword-only parameters:", x, y)

mixed_parameters(1, y=2,z=3)            # Valid: Positional and keyword arguments
mixed_parameters(1, z=3,y=2)            # Valid: Positional and keyword arguments
# mixed_parameters(x=1, y=2, z=3)          # Invalid: x must be provided positionally


# ------Standard parameter------
def standard_parameters(x, y, z):
    print("Standard parameters:", x, y, z)

standard_parameters(1, 2, 3)        # Valid: Positional arguments
standard_parameters(1, z=2, y=3)    # Valid: Positional and Keyword arguments
standard_parameters(x=1, y=2, z=3)  # Valid: Keyword arguments
