import re

# Path to your input file
input_file = "input.txt"

# Read the file content
with open(input_file, 'r') as file:
    corrupted_memory = file.read()

# Regular expressions for different instructions
mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
do_pattern = r"do\(\)"
dont_pattern = r"don't\(\)"

# Combined pattern to capture all instructions in order
combined_pattern = f"{mul_pattern}|{do_pattern}|{dont_pattern}"

# Find all matches in the corrupted memory
matches = re.finditer(combined_pattern, corrupted_memory)

# Initialize variables
enabled = True  # Mul instructions are enabled by default
total = 0

# Process each match
for match in matches:
    if match.group(1) and match.group(2):  # mul(X,Y)
        if enabled:
            x, y = int(match.group(1)), int(match.group(2))
            total += x * y
    elif match.group(0) == "do()":  # do() instruction
        enabled = True
    elif match.group(0) == "don't()":  # don't() instruction
        enabled = False

# Output the result
print("Total sum of valid enabled multiplications:", total)
