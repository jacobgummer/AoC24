import numpy as np
import sys
from collections import deque
from time import time 

file = ''

DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)] # up, right, down, left

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

def do(grid: np.ndarray):
    seen = set()
    Q = deque()
    m, n = grid.shape
    cost = 0
    for i in range(m):
        for j in range(n):
            if (i, j) in seen:
                continue
            Q = deque([(i, j)])
            area, perim = 0, 0
            while Q:
                i2, j2 = Q.popleft()
                if (i2, j2) in seen:
                    continue
                seen.add((i2, j2))
                area += 1
                for di, dj in DIRS:
                    p = i2 + di, j2 + dj
                    if is_valid(p, grid.shape) and grid[p] == grid[i2, j2]:
                        Q.append(p)
                    else:
                        perim += 1
            cost += area * perim
    return cost
    
grid = convert_to_2d(lines)
cost = do(grid)
print(cost)