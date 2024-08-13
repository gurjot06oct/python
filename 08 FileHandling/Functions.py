import sys
# 1. **`close()`**:
#    - **Description**: Closes the file.
#    - **Usage**: After you've finished working with a file, it's important to close it using this method to free up system resources.
   
# 2. **`detach()`**:
#    - **Description**: Returns the separated raw stream from the buffer.
#    - **Usage**: Useful when you want to access the underlying raw stream without the buffering mechanism provided by the file object. This method effectively disconnects the file object from its buffer.

# 3. **`fileno()`**:
#    - **Description**: Returns a number that represents the stream, from the operating system's perspective.
#    - **Usage**: Typically used for advanced I/O operations where you need to work directly with the file descriptor. This method returns an integer file descriptor associated with the file object.

# 4. **`flush()`**:
#    - **Description**: Flushes the internal buffer, ensuring that all buffered data is written to the underlying file.
#    - **Usage**: Useful when you want to ensure that all data written to the file object is immediately flushed to disk.

# 5. **`isatty()`**:
#    - **Description**: Returns whether the file stream is interactive or not.
#    - **Usage**: Determines whether the file object represents a terminal device or not. Returns `True` if the file stream is interactive (like a terminal), otherwise returns `False`.

# 6. **`read()`**:
#    - **Description**: Reads and returns the file content.
#    - **Usage**: Reads the entire content of the file and returns it as a string. You can optionally specify the number of bytes to read.

# 7. **`rename()`**:
#    - **Description**: Renames the file with a new name.
#    - **Usage**: Changes the name of the file to the specified new name. Can be useful for renaming files programmatically.

# 8. **File Handling Methods**:
#    These methods are typically used for reading, writing, and manipulating files:
#    - **`readable()`**: Returns whether the file stream can be read or not.
#    - **`readline()`**: Returns one line from the file.
#    - **`readlines()`**: Returns a list of lines from the file.
#    - **`seek(offset, whence=0)`**: Change the file position.
#    - **`seekable()`**: Returns whether the file allows us to change the file position.
#    - **`tell()`**: Returns the current file position.
#    - **`truncate(size=None)`**: Resizes the file to a specified size.
#    - **`writable()`**: Returns whether the file can be written to or not.
#    - **`write(string)`**: Writes the specified string to the file.
#    - **`writelines(lines)`**: Writes a sequence of lines to the file.



# Open the file in read mode
file = open("example.txt", "r+")

# Detach the file object
raw_stream = file.detach()

# Check if the file stream is interactive
print("\nIs TTY?:", raw_stream.isatty())
if sys.stdin.isatty():
    print("Standard input (stdin) is connected to a terminal.")
else:
    print("Standard input (stdin) is NOT connected to a terminal.")

# Flush the internal buffer ( fileObject.flush() will not do anything )
# raw stream take data in byte-like object
raw_stream.write(b"How are You?")
raw_stream.flush()
print(raw_stream.read()) # empty as stream is flushed to disk

# Get the file descriptor number
print("\nFile Descriptor:", raw_stream.fileno())

# Open the file again in write mode
file = open("example.txt", "w")


# Rename the file
import os
os.rename("example.txt", "new_example.txt")
print("\nFile renamed successfully.")

# Check if the file exists
if os.path.exists("new_example.txt"):
    print("File 'new_example.txt' exists.")
else:
    print("File 'new_example.txt' does not exist.")

# Close the file
file.close()
