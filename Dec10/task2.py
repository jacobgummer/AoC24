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
        rows.append([int(c) for c in line])
    return np.array(rows)

def is_inside_boundary(pos, boundary):
    i, j = pos
    m, n = boundary
    return 0 <= i < m and 0 <= j < n

def get_nearby(grid: np.ndarray, pos):
    coordinates = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    possible = [(pos[0] + c[0], pos[1] + c[1]) for c in coordinates]
    return [(grid[p], p) for p in possible if is_inside_boundary(p, grid.shape)]

def get_next_steps(grid: np.ndarray):
    next_steps = dict()
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            curr = grid[i,j]
            next_steps[(i, j)] = []
            nearby = get_nearby(grid, (i, j))
            for n, p in nearby:
                if curr == n - 1:
                    next_steps[(i, j)].append(p)
    return next_steps

def find_0s(grid: np.ndarray):
    positions = []
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i, j] == 0: positions.append((i,j))
    return positions

def get_rating(pos, next_steps, curr_n=0):
    if curr_n == 9:
        return 1
    possible = 0
    if not next_steps[pos]:
        return 0
    for next_pos in next_steps[pos]:
        possible += get_rating(next_pos, next_steps, curr_n + 1)
    return possible

grid = convert_to_2d(lines)
next_steps = get_next_steps(grid)
positions = find_0s(grid)
ratings = [get_rating(p, next_steps) for p in positions]
print(sum(ratings))