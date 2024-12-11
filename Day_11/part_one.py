
# Function to apply the rules and process the stones
def process_stones(stones):
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            mid = len(str(stone)) // 2
            left = int(str(stone)[:mid])
            right = int(str(stone)[mid:])
            new_stones.extend([left, right])
        else:
            new_stones.append(stone * 2024)
    return new_stones

# Read the input file with initial stone numbers
def read_input(file_path):
    with open(file_path, "r") as file:
        line = file.readline().strip()
        stones = list(map(int, line.split()))
    return stones

# Main simulation function
def simulate_blinks(file_path, num_blinks):
    stones = read_input(file_path)
    for _ in range(num_blinks):
        stones = process_stones(stones)
    return len(stones)

# Example usage
if __name__ == "__main__":
    input_file = "input.txt"  # Replace with your input file name
    num_blinks = 25
    result = simulate_blinks(input_file, num_blinks)
    print(f"Number of stones after {num_blinks} blinks: {result}")
