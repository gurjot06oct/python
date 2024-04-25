# my_package/__init__.py

# Initialization code
print("Initializing sub_package...")

# List of symbols to export when using "from my_package import *"
__all__ = ['submodule1', 'submodule2']

# Importing modules to make them accessible from the package namespace
from . import submodule1
from . import submodule2
