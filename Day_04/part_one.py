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
def count_xmas_in_grid(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    target = "XMAS"
    target_len = len(target)
    total_count = 0

    # Helper function to count occurrences in a line
    def count_in_line(line):
        return sum(line[i:i + target_len] == target for i in range(len(line) - target_len + 1))

    # Count horizontally and reverse horizontally
    for row in grid:
        total_count += count_in_line(row)
        total_count += count_in_line(row[::-1])

    # Count vertically and reverse vertically
    for col in range(cols):
        column = ''.join(grid[row][col] for row in range(rows))
        total_count += count_in_line(column)
        total_count += count_in_line(column[::-1])

    # Count diagonals (top-left to bottom-right and their reverses)
    for start in range(-rows + 1, cols):
        diagonal = ''.join(grid[row][col] for row in range(rows) for col in range(cols) if col - row == start)
        total_count += count_in_line(diagonal)
        total_count += count_in_line(diagonal[::-1])

    # Count anti-diagonals (top-right to bottom-left and their reverses)
    for start in range(rows + cols - 1):
        anti_diagonal = ''.join(grid[row][col] for row in range(rows) for col in range(cols) if row + col == start)
        total_count += count_in_line(anti_diagonal)
        total_count += count_in_line(anti_diagonal[::-1])

    return total_count

# File path to the input file
file_path = "input.txt"

# Read the grid from the file
with open(file_path, "r") as file:
    grid = [line.strip() for line in file.readlines()]

# Debug: Print the grid to confirm it is read correctly
print("Grid Read from File:")
print("\n".join(grid))

# Count all occurrences of XMAS
xmas_count = count_xmas_in_grid(grid)

# Output the result
print(f"Total occurrences of 'XMAS': {xmas_count}")