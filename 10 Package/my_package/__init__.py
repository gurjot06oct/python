# my_package/__init__.py

# Initialization code
print("Initializing my_package...")

from .module1 import *
from .module2 import *
# random_color_generator is not imported  here
# throw error, cause not exported  as wilcard  in module1.py


# `__all__` is a special variable that can be defined within a module's __init__.py file. It is used to specify a list of names that should be exported when the module is imported using the wildcard import statement from module import *.

# Add module names and functions to __all__
__all__ = ['module1', 'module2', 'random_password_generator', 'random_sentence_generator', 'random_matrix_generator']

# or

# you can achieve selective import without using the `__all__` variable by explicitly importing the names you want to expose in the `__init__.py` file.

# from . import module1
# from . import module2
# from .module1 import random_password_generator,random_color_generator
# ...