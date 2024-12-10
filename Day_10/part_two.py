def read_map(file_path):
    """
    Reads the topographic map from a file and returns it as a 2D list of integers.
    """
    with open(file_path, 'r') as f:
        return [list(map(int, line.strip())) for line in f.readlines()]

def find_trailheads_and_ratings(topographic_map):
    """
    Finds all trailheads and calculates their ratings based on the number of distinct trails.
    """
    rows = len(topographic_map)
    cols = len(topographic_map[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

    def is_valid(x, y, current_height):
        """Checks if a move to (x, y) is valid."""
        return (
            0 <= x < rows and
            0 <= y < cols and
            topographic_map[x][y] == current_height + 1
        )

    def dfs_count_paths(x, y, visited):
        """
        Performs DFS to count distinct paths from a given position to any '9'.
        """
        if (x, y) in visited:
            return 0
        visited.add((x, y))

        if topographic_map[x][y] == 9:
            visited.remove((x, y))
            return 1

        total_paths = 0
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny, topographic_map[x][y]):
                total_paths += dfs_count_paths(nx, ny, visited)

        visited.remove((x, y))
        return total_paths

    trailheads_ratings = []
    for i in range(rows):
        for j in range(cols):
            if topographic_map[i][j] == 0:  # Found a trailhead
                rating = dfs_count_paths(i, j, set())
                trailheads_ratings.append(rating)

    return trailheads_ratings

def calculate_total_rating(file_path):
    """
    Calculates the total rating for all trailheads in the topographic map.
    """
    topographic_map = read_map(file_path)
    trailheads_ratings = find_trailheads_and_ratings(topographic_map)
    return sum(trailheads_ratings)

# File input (replace 'input.txt' with your actual input file path)
input_file = 'input.txt'
total_rating = calculate_total_rating(input_file)
print(f"Total rating of all trailheads: {total_rating}")
