from collections import Counter

def simulate_blinks_count(stones, num_blinks):
    """
    Simulate the evolution of stones over a given number of blinks.

    Args:
        stones (list of int): The initial list of stone values.
        num_blinks (int): The number of blinks to simulate.

    Returns:
        int: The total number of stones after all blinks.
    """
    # Count the initial stones
    stone_counts = Counter(stones)

    for _ in range(num_blinks):
        new_counts = Counter()
        for stone, count in stone_counts.items():
            if stone == 0:
                new_counts[1] += count
            elif len(str(stone)) % 2 == 0:  # Even number of digits
                stone_str = str(stone)
                mid = len(stone_str) // 2
                left = int(stone_str[:mid])
                right = int(stone_str[mid:])
                new_counts[left] += count
                new_counts[right] += count
            else:
                new_counts[stone * 2024] += count
        stone_counts = new_counts

    return sum(stone_counts.values())

def main():
    """
    Main function to read input, simulate blinks, and output results.
    """
    # Define the path to the input file
    file_path = "input.txt"

    try:
        # Read initial stones from the file
        with open(file_path, 'r') as file:
            content = file.read().strip()

        # Extract initial stones (assume they are space-separated integers)
        initial_stones = list(map(int, content.split()))

        # Simulate blinks
        num_blinks = 75
        total_stones = simulate_blinks_count(initial_stones, num_blinks)

        # Output the number of stones
        print("Number of stones after 75 blinks:", total_stones)
    except FileNotFoundError:
        print(f"Error: The file at '{file_path}' was not found.")
    except ValueError:
        print("Error: The input file contains invalid data. Please ensure it contains space-separated integers.")

if __name__ == "__main__":
    main()