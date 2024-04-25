import  os
# File Path
file_path = "Example.txt"


# Read Mode ('r'):
    # Opens a file for reading.
    # The file pointer is placed at the beginning of the file.
    # Use this mode when you only need to read data from the file and do not intend to modify it.
# Write Mode ('w'):
    # Opens a file for writing.
    # If the file already exists, its contents are truncated (i.e., deleted), and a new empty file is created.
    # If the file does not exist, a new file is created.
    # Use this mode when you want to write data to a file, overwriting any existing content.
# Append Mode ('a'):
    # Opens a file for writing.
    # If the file already exists, new data is appended to the end of the file.
    # If the file does not exist, a new file is created.
    # Use this mode when you want to add data to the end of an existing file without overwriting its content.
# Binary Mode ('b'):
    # Opens a file in binary mode.
    # This mode is used when dealing with non-text files or when you want to read/write binary data (e.g., images, audio files).
    # It ensures that no translation of newline characters is performed, and the data is read/written as-is.
# Read/Write Mode ('r+'):
    # Opens a file for both reading and writing.
    # The file pointer is placed at the beginning of the file.
    # Use this mode when you need to both read from and write to a file without truncating its content.
# Write/Read Mode ('w+'):
    # Opens a file for reading and writing.
    # If the file exists, its contents are truncated, and a new empty file is created.
    # Use this mode when you need to both read from and write to a file, starting with an empty file.
# Append/Read Mode ('a+'):
    # Opens a file for reading and writing.
    # If the file exists, new data is appended to the end of the file.
    # Use this mode when you need to both read from and append to a file, preserving its existing content.


# Writing to a File
with open(file_path, "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a sample text file.\n")
    file.write("Python is awesome!\n")
    # Reading here gives an Error (UnsupportedOperation)

# File is automatically closed after the 'with' block or use file.close()


# read():
    # The read() method reads the entire contents of the file as a single string.
    # It reads the file from the current position of the file pointer (cursor) until the end of the file.
    # If you call read() again on the same file object, it will return an empty string since the file pointer is already at the end of the file.
# readline():
    # The readline() method reads a single line from the file.
    # It reads from the current position of the file pointer until it encounters a newline character ('\n') or reaches the end of the file.
    # Each time you call readline(), it moves the file pointer to the beginning of the next line.
# readlines():
    # The readlines() method reads all the lines of the file and returns them as a list of strings.
    # Each string in the list represents one line of the file, including the newline character ('\n') at the end of each line.
    # If the file is large, this method can consume a lot of memory because it reads the entire file into memory at once.


# Reading from a File
with open(file_path, "r") as file:
    # Read the entire file
    content = file.read()
    print("File Content:")
    print(content)

    # Read line by line
    print("\nLines:")
    file.seek(0)  # Reset file pointer to beginning
    # print(*file) can also be used to print file content
    for line in file:
        print(line.strip()) # .strip() to remove \n
    # Writing here gives an Error (UnsupportedOperation)

# Appending to a File
with open(file_path, "a") as file:
    file.write("Appending new content...\n")
    file.write("It's easy to learn python.\n")
    file.seek(0)
    file.write("This line will not be written as append only works at the end of file.")
    # Reading here gives an Error (UnsupportedOperation)

# Reading from the File after Appending
with open(file_path, "r") as file:
    content_after_append = file.read()
    print("\nFile Content After Appending:")
    print(content_after_append)


# Writing to a File (w+ mode)
with open(file_path, "w+") as file:
    file.write("Hello, World!\n")
    file.write("This is a sample text file.\n")
    file.write("Python is awesome!\n")


# Reading from a File (r+ mode)
with open(file_path, "r+") as file:
    # Read the entire file
    content = file.read()
    print("File Content (r+ mode):")
    print(content)

    # Seek to the beginning and overwrite the file content
    file.seek(0)
    file.write("Overwriting the content...\n")

    # Seek to the end and append new content
    file.seek(0, os.SEEK_END)
    file.write("Appending new content...\n")

# Reading from the File after Modification
with open(file_path, "r") as file:
    content_after_modify = file.read()
    print("\nFile Content After Modification:")
    print(content_after_modify)

# Reading from the File (a+ mode)
with open(file_path, "a+") as file:
    file.write("This is the Appended Line.\n")
    file.seek(0)
    file.write("f.write() in append mode will only be written at the end even if you seek to 0")
    file.seek(0)
    content_after_append = file.read()
    print("\nFile Content After Appending:")
    print(content_after_append)
    

# Open the file in binary read mode ("rb")
with open(file_path, "rb") as file:
    # Read the contents of the file
    contents = file.read()
    # Print the contents to the console
    print(contents)


# Deleting the File
import os
os.remove(file_path)
print("\nFile deleted successfully.")
