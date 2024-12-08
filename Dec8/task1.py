import numpy as np
import itertools
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

def create_dict(grid: np.ndarray):
    d: dict[str, list[tuple[int, int]]] = dict()

    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i,j] != '.':
                if not d.get(str(grid[i,j])): d[str(grid[i,j])] = []
                d[str(grid[i,j])].append((i, j)) 
            
    return d

def get_all_pairs(d: dict[str, list[tuple[int, int]]]):
    all_pairs = dict()
    for k in d.keys():
        pairs = list(itertools.combinations(d[k], 2))
        all_pairs[k] = pairs
    return all_pairs

def is_inside_boundary(pos, boundary):
    i, j = pos
    m, n = boundary
    return 0 <= i < m and 0 <= j < n

def delta_pos(p1, p2):
    return p1[0] - p2[0], p1[1] - p2[1]

def get_antinodes(all_pairs: dict, boundary):
    antinodes_pos = set()
    for k in all_pairs.keys():
        for p1, p2 in all_pairs[k]:
            dx, dy = delta_pos(p1, p2)
            new_p1, new_p2 = (p1[0] + dx, p1[1] + dy), (p2[0] - dx, p2[1] - dy)
            if is_inside_boundary(new_p1, boundary): antinodes_pos.add(new_p1)
            if is_inside_boundary(new_p2, boundary): antinodes_pos.add(new_p2)
    return antinodes_pos

grid = convert_to_2d(lines)
d = create_dict(grid)
all_pairs = get_all_pairs(d)
antinodes = get_antinodes(all_pairs, grid.shape)
print(len(antinodes))