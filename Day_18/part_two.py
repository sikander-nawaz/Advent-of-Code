from collections import deque

def read_input_file(file_path):
    """Reads the input file and returns a list of (x, y) tuples."""
    with open(file_path, 'r') as file:
        byte_positions = [
            tuple(map(int, line.strip().split(','))) for line in file.readlines()
        ]
    return byte_positions

def is_path_blocked(grid, start, end):
    """Checks if there is a path from start to end using BFS."""
    grid_size = len(grid)
    queue = deque([start])
    visited = set()
    visited.add(start)
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Down, Right, Up, Left
    
    while queue:
        x, y = queue.popleft()
        
        if (x, y) == end:
            return False  # Path exists
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < grid_size and 0 <= ny < grid_size and grid[ny][nx] == '.' and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny))
    
    return True  # No path exists

def find_first_blocking_byte(grid_size, byte_positions, start, end):
    """Finds the first byte that blocks the path to the exit."""
    # Create the grid
    grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]
    
    for step, (x, y) in enumerate(byte_positions, 1):
        # Mark the current byte position as corrupted
        grid[y][x] = '#'
        
        # Check if the path is blocked
        if is_path_blocked(grid, start, end):
            return f"{x},{y}"  # Return the coordinates of the blocking byte

    return None  # No byte blocked the path

# Main Function
def main():
    file_path = 'input.txt'  # Path to your input file
    byte_positions = read_input_file(file_path)
    
    # Problem Parameters
    grid_size = 71  # For the full problem
    start = (0, 0)
    end = (70, 70)
    
    # Find the first blocking byte
    blocking_byte = find_first_blocking_byte(grid_size, byte_positions, start, end)
    print(blocking_byte)

if __name__ == "__main__":
    main()
