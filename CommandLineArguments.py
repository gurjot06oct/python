import sys

print(sys.argv)
# Check the length of sys.argv to ensure at least one command-line argument is provided
if len(sys.argv) < 2:
    print("Usage: python script.py <arg1> [<arg2> ...]")
    sys.exit(1)  # Exit the script with a non-zero status code

# The first command-line argument (sys.argv[0]) is the script name, so we start from index 1
for i, arg in enumerate(sys.argv[1:]):
    print(f"Argument {i}: {arg}")


# library - getopt, argparse

import getopt, sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "hi:o:", ["ifile=", "ofile="])
except getopt.GetoptError:
    print('example_getopt.py -i <inputfile> -o <outputfile>')
    sys.exit(2)

input_file = ''
output_file = ''

for opt, arg in opts:
    if opt == '-h':
        print('example_getopt.py -i <inputfile> -o <outputfile>')
        sys.exit()
    elif opt in ("-i", "--ifile"):
        input_file = arg
    elif opt in ("-o", "--ofile"):
        output_file = arg

print('Input file is:', input_file)
print('Output file is:', output_file)
