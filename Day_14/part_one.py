def read_input(file_path):
    """Reads the input file and parses robot positions and velocities."""
    robots = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            pos = tuple(map(int, parts[0][2:].split(',')))
            vel = tuple(map(int, parts[1][2:].split(',')))
            robots.append((pos, vel))
    return robots


def update_position(position, velocity, width, height):
    """Updates the robot's position considering wrapping around the edges."""
    x = (position[0] + velocity[0]) % width
    y = (position[1] + velocity[1]) % height
    return x, y


def simulate(robots, width, height, seconds):
    """Simulates the motion of robots for a given number of seconds."""
    grid = [[0 for _ in range(width)] for _ in range(height)]

    for pos, vel in robots:
        for _ in range(seconds):
            pos = update_position(pos, vel, width, height)
        grid[pos[1]][pos[0]] += 1

    return grid


def count_robots_in_quadrants(grid, width, height):
    """Counts the number of robots in each quadrant, excluding middle rows and columns."""
    half_width, half_height = width // 2, height // 2
    quadrants = [0, 0, 0, 0]

    for y, row in enumerate(grid):
        for x, count in enumerate(row):
            if count > 0:
                if x == half_width or y == half_height:
                    continue
                elif x < half_width and y < half_height:
                    quadrants[0] += count  # Top-left
                elif x >= half_width and y < half_height:
                    quadrants[1] += count  # Top-right
                elif x < half_width and y >= half_height:
                    quadrants[2] += count  # Bottom-left
                elif x >= half_width and y >= half_height:
                    quadrants[3] += count  # Bottom-right

    return quadrants


def main():
    file_path = "input.txt"  # Update this path if your input file is named differently
    width, height = 101, 103
    seconds = 100

    robots = read_input(file_path)
    grid = simulate(robots, width, height, seconds)
    quadrants = count_robots_in_quadrants(grid, width, height)

    safety_factor = 1
    for count in quadrants:
        safety_factor *= count

    print("Quadrant counts:", quadrants)
    print("Safety factor:", safety_factor)


if __name__ == "__main__":
    main()
