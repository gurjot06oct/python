file_path = "ReadMode.txt"

# Read Mode ('r'):
    # Opens a file for reading.
    # The file pointer is placed at the beginning of the file.
    # Use this mode when you only need to read data from the file and do not intend to modify it.
    # You cannot write in this mode.
    # If file does not exist, then Error

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