import re

# Path to your input file
input_file = "input.txt"

# Read the file content
with open(input_file, 'r') as file:
    corrupted_memory = file.read()

# Regular expression to find valid mul(X,Y) instructions
pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

# Find all matches in the corrupted memory
matches = re.findall(pattern, corrupted_memory)

# Compute the sum of all valid multiplication results
total = sum(int(x) * int(y) for x, y in matches)

# Output the result
print("Total sum of valid multiplications:", total)
