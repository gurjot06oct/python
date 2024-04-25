# my_package/__init__.py

# Initialization code
print("Initializing my_package...")

# List of symbols to export when using "from my_package import *"
__all__ = ['module1', 'module2','sub_package']

# Importing modules to make them accessible from the package namespace
from . import module1
from . import module2
from . import sub_package