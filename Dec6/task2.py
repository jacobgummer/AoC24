import numpy as np
import sys

file = ''

if len(sys.argv) != 2:
    print("Usage: python3 task2.py [i|t]")
    sys.exit(1)

argument = sys.argv[1]

if argument == "i":
    file = 'input'
elif argument == "t":
    file = 'test'
else:
    print("Invalid argument. Use 'i' or 't'.")
    sys.exit(1)

input = open(f'./{file}.txt', 'r')
lines = input.read().splitlines()
input.close()

def convert_to_2d(lines):
    rows = []
    for line in lines:
        rows.append([c for c in line])
    return np.array(rows)

def is_inside_boundary(pos, boundary):
    i, j = pos
    m, n = boundary
    return 0 <= i < m and 0 <= j < n

def get_next(pos, dir):
    return pos[0] + dir[0], pos[1] + dir[1]

def move(grid, start_pos):
    curr_pos = start_pos
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    dir_i = 0
    visited = [curr_pos]
    
    while is_inside_boundary(curr_pos, grid.shape):
        next_pos = get_next(curr_pos, dirs[dir_i])
        if is_inside_boundary(next_pos, grid.shape) and grid[next_pos] == '#':
            dir_i = (dir_i + 1) % 4
        curr_pos = get_next(curr_pos, dirs[dir_i])
        if curr_pos not in visited: visited.append(curr_pos)
    return visited[:-1]

def is_loop(grid: np.ndarray, start_pos, obs_pos):
    new_grid = grid.copy()
    new_grid[obs_pos] = '#'
    visited = set()
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    dir_i = 0
    curr_dir = directions[dir_i]
    curr_pos = start_pos
    boundary = new_grid.shape
    
    while True:
        next_pos = get_next(curr_pos, curr_dir)
        if not is_inside_boundary(next_pos, boundary):
            return False
        if new_grid[next_pos] == '#':
            dir_i = (dir_i + 1) % len(directions)
            curr_dir = directions[dir_i]
        else:
            curr_pos = next_pos
        new_visit = curr_pos, curr_dir
        if new_visit in visited:
            return True
        visited.add(new_visit)
        
def check_for_loops(grid, path):
    start_pos = path[0]
    n_places = 0
    for pos in path[1:]:
        n_places += is_loop(grid, start_pos, pos)
    return n_places

grid = convert_to_2d(lines)
start_r, start_c = np.where(grid == '^')
start_pos = int(start_r[0]), int(start_c[0])

path = move(grid, start_pos)
n_places = check_for_loops(grid, path)
print(n_places)