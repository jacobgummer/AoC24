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

def is_valid(i, j, m, n):
    return i >= 0 and j >= 0 and i < m and j < n

def search_MAS(grid, x, y, dx, dy, reverse=False):
    m, n = grid.shape
    word = 'MAS' if not reverse else 'SAM'
    
    x, y = x + dx, y + dy
    
    k = 1
    while k < 3:
        if not is_valid(x, y, m, n) or grid[x, y] != word[k]:
            break
        x, y = x + dx, y + dy
        k += 1
    if k == 3:
        return 1
    return 0

def search_from_left(grid, r, c):
    if grid[r, c] == 'M':
        return bool(search_MAS(grid, r, c, 1, -1))
    elif grid[r, c] == 'S':
        return bool(search_MAS(grid, r, c, 1, -1, True))
    return False

def search_from_right(grid, r, c):
    if grid[r, c] == 'M':
        return search_MAS(grid, r, c, -1, -1)
    elif grid[r, c] == 'S':
        return search_MAS(grid, r, c, -1, -1, True)
    return 0

def loop_through_grid(grid):
    m, n = grid.shape
    
    total = 0
    for i in range(m):
        for j in range(n):
            if search_from_left(grid, i, j):
                total += search_from_right(grid, i + 2, j)
    return total

grid = convert_to_2d(lines)
total = loop_through_grid(grid)
print(total)            