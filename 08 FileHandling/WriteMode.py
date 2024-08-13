file_path = "WriteMode.txt"

# Write Mode ('w'):
    # Opens a file for writing.
    # If the file already exists, its contents are truncated (i.e., deleted), and a new empty file is created.
    # If the file does not exist, a new file is created.
    # You cannot read in this mode.
    # Use this mode when you want to write data to a file, overwriting any existing content.

# Writing to a File
with open(file_path, "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a sample text file.\n")
    file.write("Python is awesome!\n")
    # Reading here gives an Error (UnsupportedOperation)