# Packages:
    # A package is a collection of modules in directories.
    # It's a way of organizing related modules into a single hierarchy.
    # Packages are identified by the presence of an __init__.py file in the package directory.
    # Packages can contain sub-packages, which are simply subdirectories containing their own __init__.py files.


# Importing methods from the main package
from my_package import module1, module2

# Importing methods from the sub-package
from my_package.sub_package import submodule1, submodule2

# Using methods from the main package
module1.greet("John")
print(module2.square(5))

# Using methods from the sub-package
submodule1.greet("Alice")
submodule2.greet("Devis")

