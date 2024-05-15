# Packages:
    # A package is a collection of modules in directories.
    # It's a way of organizing related modules into a single hierarchy.
    # Packages are identified by the presence of an __init__.py file in the package directory.
    # Packages can contain sub-packages, which are simply subdirectories containing their own __init__.py files.


from my_package.module1 import *
random_password_generator(7)
# random_color_generator()
# throw error, cause not exported  as wilcard  in module1.py
