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
        rows.append([int(c) for c in line])
    return np.array(rows)

def is_inside_boundary(pos, boundary):
    i, j = pos
    m, n = boundary
    return 0 <= i < m and 0 <= j < n

def nearby(grid: np.ndarray, pos):
    coordinates = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    possible = [(pos[0] + c[0], pos[1] + c[1]) for c in coordinates]
    return [(grid[p], p) for p in possible if is_inside_boundary(p, grid.shape)]

def find_9s(grid: np.ndarray):
    positions = []
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i, j] == 9: positions.append((i,j))
    return positions

def leads_to_0(grid, pos, curr_n=9):
    if curr_n == 0:
        return set([pos])
    possible = set()
    for n, p in nearby(grid, pos):
        if n == curr_n - 1:
            leads = leads_to_0(grid, p, n)
            possible = possible.union(leads)
    return possible

def test_9s(grid: np.ndarray, positions: list):
    all_trailheads = dict()
    for pos in positions:
        trailheads = leads_to_0(grid, pos)
        for t in trailheads:
            if not all_trailheads.get(t):
                all_trailheads[t] = 0
            all_trailheads[t] += 1
    return all_trailheads
        
        
grid = convert_to_2d(lines)
positions = find_9s(grid)
all_trailheads = test_9s(grid, positions)
print(sum(list(all_trailheads.values())))
