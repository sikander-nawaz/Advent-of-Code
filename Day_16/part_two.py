from collections import deque
from typing import List, Set, Tuple

class MazeSolver:
    def __init__(self, maze: List[List[str]]):
        self.maze = maze
        self.height = len(maze)
        self.width = len(maze[0])
        self.start, self.end = self._find_start_end()

    def _find_start_end(self) -> Tuple[Tuple[int, int], Tuple[int, int]]:
        start = end = None
        for y in range(self.height):
            for x in range(self.width):
                if self.maze[y][x] == 'S':
                    start = (y, x)
                elif self.maze[y][x] == 'E':
                    end = (y, x)
        return start, end

    def find_optimal_tiles(self) -> int:
        # Directions: right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # First pass: Find minimum score to end from each position and direction
        best_scores = {}  # (y, x, dir) -> min_score
        queue = deque([(self.start[0], self.start[1], 0, 0)])  # y, x, dir, score
        min_end_score = float('inf')
        
        while queue:
            y, x, dir, score = queue.popleft()
            
            if score >= min_end_score:
                continue
                
            state = (y, x, dir)
            if state in best_scores and best_scores[state] <= score:
                continue
            best_scores[state] = score
            
            # Found end
            if (y, x) == self.end:
                min_end_score = min(min_end_score, score)
                continue
            
            # Try moving forward
            ny, nx = y + directions[dir][0], x + directions[dir][1]
            if (0 <= ny < self.height and 0 <= nx < self.width and 
                self.maze[ny][nx] != '#'):
                queue.append((ny, nx, dir, score + 1))
            
            # Try turning
            queue.append((y, x, (dir - 1) % 4, score + 1000))
            queue.append((y, x, (dir + 1) % 4, score + 1000))
        
        # Second pass: Find tiles that are part of optimal paths
        optimal_tiles = set()
        visited = set()
        queue = deque([(self.start[0], self.start[1], 0, 0, {(self.start[0], self.start[1])})])
        
        while queue:
            y, x, dir, score, path = queue.popleft()
            
            if score > min_end_score:
                continue
                
            state = (y, x, dir)
            if score > best_scores.get(state, float('inf')):
                continue
                
            if (y, x) == self.end and score == min_end_score:
                optimal_tiles.update(path)
                continue
            
            # Try moving forward
            ny, nx = y + directions[dir][0], x + directions[dir][1]
            if (0 <= ny < self.height and 0 <= nx < self.width and 
                self.maze[ny][nx] != '#'):
                new_path = path | {(ny, nx)}
                queue.append((ny, nx, dir, score + 1, new_path))
            
            # Try turning
            queue.append((y, x, (dir - 1) % 4, score + 1000, path.copy()))
            queue.append((y, x, (dir + 1) % 4, score + 1000, path.copy()))
        
        return len(optimal_tiles)

def visualize_path(maze: List[List[str]], optimal_tiles: Set[Tuple[int, int]]) -> None:
    for y in range(len(maze)):
        for x in range(len(maze[0])):
            if (y, x) in optimal_tiles:
                if maze[y][x] in ['S', 'E']:
                    print(maze[y][x], end='')
                else:
                    print('O', end='')
            else:
                print(maze[y][x], end='')
        print()

def main():
    input_file = "input.txt"  # Replace with the actual input file path
    with open(input_file, 'r') as file:
        maze = [list(line.strip()) for line in file if line.strip()]
    
    solver = MazeSolver(maze)
    result = solver.find_optimal_tiles()
    print(f"Number of tiles in optimal paths: {result}")

if __name__ == "__main__":
    main()
