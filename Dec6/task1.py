import numpy as np
import sys

file = ''

if len(sys.argv) != 2:
    print("Usage: python3 task1.py [i|t]")
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

grid = convert_to_2d(lines)
start_r, start_c = np.where(grid == '^')
start_pos = int(start_r[0]), int(start_c[0])

def is_inside_boundary(pos, boundary):
    i, j = pos
    m, n = boundary
    return i >= 0 and i < m and j >= 0 and j < n

def check_next(pos, dir):
    return pos[0] + dir[0], pos[1] + dir[1]

def move(grid, start_pos):
    curr_pos = start_pos
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    dir_i = 0
    visited = [curr_pos]
    
    while is_inside_boundary(curr_pos, grid.shape):
        next_pos = check_next(curr_pos, dirs[dir_i])
        if is_inside_boundary(next_pos, grid.shape) and grid[next_pos] == '#':
            dir_i = (dir_i + 1) % 4
        curr_pos = check_next(curr_pos, dirs[dir_i])
        if curr_pos not in visited: visited.append(curr_pos)
    return len(visited) - 1

steps = move(grid, start_pos)
print(steps)