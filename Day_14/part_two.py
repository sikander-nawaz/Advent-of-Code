def parse_input(filename):
    """
    Parse input file to extract robot positions and velocities.
    """
    robots = []
    with open(filename, 'r') as f:
        for line in f:
            pos_str, vel_str = line.strip().split(' ')
            px, py = map(int, pos_str[2:].split(','))
            vx, vy = map(int, vel_str[2:].split(','))
            robots.append(((px, py), (vx, vy)))
    return robots

def simulate_robots(robots, time, width, height):
    """
    Simulate robot movements and count robot positions after given time.
    """
    grid = [[0 for _ in range(width)] for _ in range(height)]

    for (px, py), (vx, vy) in robots:
        final_x = (px + vx * time) % width
        final_y = (py + vy * time) % height
        grid[final_y][final_x] += 1

    return grid

def is_christmas_tree(grid):
    """
    Check if the robot positions form a Christmas tree pattern.
    """
    tree_pattern = [
        [0, 0, 1, 0, 0],
        [0, 1, 1, 1, 0],
        [1, 1, 1, 1, 1],
    ]

    height = len(grid)
    width = len(grid[0])

    for y in range(height - len(tree_pattern)):
        for x in range(width - len(tree_pattern[0])):
            match = True
            for dy, row in enumerate(tree_pattern):
                for dx, val in enumerate(row):
                    if val == 1 and grid[y + dy][x + dx] == 0:
                        match = False
                        break
                if not match:
                    break
            if match:
                return True

    return False

def find_christmas_tree_time(filename, max_time=10000, width=101, height=103):
    """
    Find the earliest time when robots form a Christmas tree pattern.
    """
    robots = parse_input(filename)

    for time in range(max_time):
        grid = simulate_robots(robots, time, width, height)
        if is_christmas_tree(grid):
            return time

    return -1

result = find_christmas_tree_time('input.txt')
print("Seconds until Christmas Tree Pattern:", result)
