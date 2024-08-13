# Reading binary data from a file in 'rb' mode
with open('BinaryData.bin', 'rb') as f:
    binary_data = f.read()
    print(binary_data)
    # Do something with the binary data, like processing or displaying the image



# Writing binary data to a file in 'wb' mode
binary_data_to_write = b'\x48\x65\x6c\x6c\x6f\x20\x57\x6f\x72\x6c\x64'  # Example binary data (Hello World)
with open('BinaryData.bin', 'wb') as f:
    f.write(binary_data_to_write)
    # Binary data has been written to the file
