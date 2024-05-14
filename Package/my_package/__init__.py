# my_package/__init__.py

# Initialization code
print("Initializing my_package...")

# `__all__` is a special variable that can be defined within a module's __init__.py file. It is used to specify a list of names that should be exported when the module is imported using the wildcard import statement from module import *.
# __all__ = ['module1', 'module2','sub_package']

# you can achieve selective import without using the `__all__` variable by explicitly importing the names you want to expose in the `__init__.py` file.

from .module1 import *
# from . import module2