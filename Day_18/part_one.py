from collections import deque

def read_input_file(file_path):
    """Reads the input file and returns a list of (x, y) tuples."""
    with open(file_path, 'r') as file:
        byte_positions = [
            tuple(map(int, line.strip().split(','))) for line in file.readlines()
        ]
    return byte_positions

def min_steps_to_exit(grid_size, byte_positions, start, end, steps_to_simulate=1024):
    """Simulates falling bytes and calculates the shortest path using BFS."""
    # Create the grid
    grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]
    
    # Mark corrupted positions
    for i, (x, y) in enumerate(byte_positions[:steps_to_simulate]):
        grid[y][x] = '#'
    
    # BFS to find shortest path
    def bfs(start, end):
        queue = deque([(start[0], start[1], 0)])  # (x, y, steps)
        visited = set()
        visited.add(start)
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Down, Right, Up, Left
        
        while queue:
            x, y, steps = queue.popleft()
            
            # Check if we've reached the destination
            if (x, y) == end:
                return steps
            
            # Explore neighbors
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                # Check bounds, corruption, and visited status
                if 0 <= nx < grid_size and 0 <= ny < grid_size and grid[ny][nx] == '.' and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny, steps + 1))
        
        return -1  # If no path found
    
    # Find shortest path
    return bfs(start, end)

# Main Function
def main():
    file_path = 'input.txt'  # Path to your input file
    byte_positions = read_input_file(file_path)
    
    # Problem Parameters
    grid_size = 71  # For the full problem
    start = (0, 0)
    end = (70, 70)
    steps_to_simulate = 1024  # Simulate first 1024 bytes
    
    # Run simulation
    steps = min_steps_to_exit(grid_size, byte_positions, start, end, steps_to_simulate)
    print(f"Minimum steps to exit: {steps}")

if __name__ == "__main__":
    main()
