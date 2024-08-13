file_path = "AppendMode.txt"

# Append Mode ('a'):
    # Opens a file for writing.
    # If the file already exists, new data is appended to the end of the file.
    # If the file does not exist, a new file is created.
    # Use this mode when you want to add data to the end of an existing file without overwriting its content.

# Appending to a File
with open(file_path, "a") as file:
    file.write("Appending new content...\n")
    file.write("It's easy to learn python.\n")
    file.seek(0)
    file.write("This line will written at the end as append only works at the end of file.")
    # Reading here gives an Error (UnsupportedOperation)