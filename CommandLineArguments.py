import sys

# Check the length of sys.argv to ensure at least one command-line argument is provided
if len(sys.argv) < 2:
    print("Usage: python script.py <arg1> [<arg2> ...]")
    sys.exit(1)  # Exit the script with a non-zero status code

# The first command-line argument (sys.argv[0]) is the script name, so we start from index 1
for i, arg in enumerate(sys.argv[1:]):
    print(f"Argument {i}: {arg}")
