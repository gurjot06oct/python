import os
# 1. **`r+` mode**:
#    - This mode opens a file for both reading and writing.
#    - It places the file pointer at the beginning of the file.
#    - If the file does not exist, it raises a `FileNotFoundError`.
#    - If the file exists, any data written to the file will overwrite the existing content as it starts at zero
#    - Reading from the file is allowed, and changes made to the file are immediately visible.
#    - It's important to note that using `r+` mode requires that the file already exists.


# 2. **`w+` mode**:
#    - This mode opens a file for both reading and writing.
#    - It truncates the file to zero bytes if it exists, or creates a new file if it does not exist.
#    - It places the file pointer at the beginning of the file.
#    - Reading from the file is allowed.
#    - Any data written to the file will overwrite the existing content.
#    - It's commonly used to create a new file or to truncate an existing file and start writing from the beginning.
#    - If you want to append data to the end of the file instead of overwriting existing content, you should use `a+` mode.

# 3. **`a+` mode**:
#    - This mode opens a file for both reading and appending.
#    - It places the file pointer at the end of the file, allowing you to append data to the file.
#    - If the file does not exist, it creates a new file.
#    - Reading from the file is allowed, and changes made to the file by other processes will not be visible.
#    - Writing to the file will append data to the end without overwriting existing content.
#    - It's useful when you want to open a file for both reading and writing, and you want to append data to the end of the file.

# Reading from a File (r+ mode)
with open("example.txt", "r+") as file:
    # Here pointer is at 0 and writing will overwrite the file
    file.write("Hella ")
    # Read the file after 'Hella'
    content = file.read() # ", World! ...."
    print("File Content (r+ mode):")
    print(content)

    # Seek to the beginning and overwrite the file content
    file.seek(0)
    file.write("Overwriting the content...\n")

    # Seek to the end and append new content
    file.seek(0, os.SEEK_END)
    file.write("Appending new content...\n")




# Example using w+ mode
with open('example.txt', 'w+') as f:
    data = f.read()  # Read data from the file
    # w+ truncates the File (i.e. deletes the data) therefore data is empty
    print("Empty Data",data)
    f.write('New Data')  # Write data to the file



# Reading from the File (a+ mode)
with open("example.txt", "a+") as file:
    file.write("This is the Appended Line.\n")
    file.seek(0)
    file.write("f.write() in append mode will only be written at the end even if you seek to 0")
    file.seek(0)
    content_after_append = file.read()
    print("\nFile Content After Appending:")
    print(content_after_append)