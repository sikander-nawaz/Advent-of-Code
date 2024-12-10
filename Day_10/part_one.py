def read_map(file_path):
    """
    Reads the topographic map from a file and returns it as a 2D list of integers.
    """
    with open(file_path, 'r') as f:
        return [list(map(int, line.strip())) for line in f.readlines()]

def find_trailheads_and_scores(topographic_map):
    """
    Finds all trailheads and calculates their scores based on reachable 9s.
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

    def bfs_trailhead(start_x, start_y):
        """Performs BFS to calculate the number of reachable 9s from a trailhead."""
        visited = set()
        queue = [(start_x, start_y)]
        reachable_nines = set()

        while queue:
            x, y = queue.pop(0)

            if (x, y) in visited:
                continue
            visited.add((x, y))

            # If this is a '9', add it to reachable_nines
            if topographic_map[x][y] == 9:
                reachable_nines.add((x, y))

            # Explore neighbors
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if is_valid(nx, ny, topographic_map[x][y]):
                    queue.append((nx, ny))

        return len(reachable_nines)

    trailheads_scores = []
    for i in range(rows):
        for j in range(cols):
            if topographic_map[i][j] == 0:  # Found a trailhead
                score = bfs_trailhead(i, j)
                trailheads_scores.append(score)

    return trailheads_scores

def calculate_total_score(file_path):
    """
    Calculates the total score for all trailheads in the topographic map.
    """
    topographic_map = read_map(file_path)
    trailheads_scores = find_trailheads_and_scores(topographic_map)
    return sum(trailheads_scores)

# File input (replace 'input.txt' with your actual input file path)
input_file = 'input.txt'
total_score = calculate_total_score(input_file)
print(f"Total score of all trailheads: {total_score}")
