# In Python, the with statement is used to simplify exception handling and resource management, particularly for objects that support the context management protocol. The with statement ensures that certain operations are properly initialized and finalized, even if exceptions occur during the execution of the block of code.

with open('example.txt', 'w') as f:
    f.write('Hello, world!')