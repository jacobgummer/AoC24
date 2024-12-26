import numpy as np
import sys
from collections import deque

DIRS = {'up': (-1, 0), 'right': (0, 1), 'down': (1, 0), 'left': (0, -1)} # up, right, down, left

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

def is_valid(point, boundary):
    i, j = point
    m, n = boundary
    return 0 <= i < m and 0 <= j < n

def check_corners(region: list[tuple[int, int]], point: tuple[int, int]):
    region = set(region)

    def convert_2d_to_tuple(array):
        return tuple(array)

    ul = convert_2d_to_tuple(np.asarray(point) - 1)
    ur = convert_2d_to_tuple(np.asarray(point) + np.array([-1, 1]))
    dl = convert_2d_to_tuple(np.asarray(point) + np.array([1, -1]))
    dr = convert_2d_to_tuple(np.asarray(point) + 1)

    keys = ['up', 'right', 'down', 'left']
    other_dirs = [(point[0] + dx, point[1] + dy) for dx, dy in DIRS.values()]
    other_pos = {s: d for s, d in zip(keys, other_dirs)}

    def is_corner_valid(corner_set, diff_set, corner):
        return (diff_set == corner_set or diff_set == {corner} or corner_set.intersection(region) == {corner})

    c_ul = 1 if is_corner_valid({other_pos['left'], ul, other_pos['up']}, {other_pos['left'], ul, other_pos['up']}.difference(region), ul) else 0
    c_ur = 1 if is_corner_valid({other_pos['up'], ur, other_pos['right']}, {other_pos['up'], ur, other_pos['right']}.difference(region), ur) else 0
    c_dr = 1 if is_corner_valid({other_pos['right'], dr, other_pos['down']}, {other_pos['right'], dr, other_pos['down']}.difference(region), dr) else 0
    c_dl = 1 if is_corner_valid({other_pos['left'], dl, other_pos['down']}, {other_pos['left'], dl, other_pos['down']}.difference(region), dl) else 0

    corners = c_ul + c_ur + c_dr + c_dl

    return corners

def check_regions(regions: list[list[tuple[int, int]]]):
    cost = 0
    
    for region in regions:
        area = len(region)
        sides = 0
        for p in region:
            sides += check_corners(region, p)
        cost += area * sides

    return cost

def do(grid: np.ndarray):
    seen = set()
    Q = deque()
    id = 0
    regions = []
    m, n = grid.shape
    for i in range(m):
        for j in range(n):
            if (i, j) in seen:
                continue
            Q = deque([(i, j)])
            regions.append([])
            area = 0
            while Q:
                i2, j2 = Q.popleft()
                if (i2, j2) in seen:
                    continue
                seen.add((i2, j2))
                regions[id].append((i2, j2))
                area += 1
                for di, dj in DIRS.values():
                    p = i2 + di, j2 + dj
                    if is_valid(p, grid.shape) and grid[p] == grid[i2, j2]:
                        Q.append(p)
            id += 1
    cost = check_regions(regions)
    return cost
    
grid = convert_to_2d(lines)
cost = do(grid)
print(cost)