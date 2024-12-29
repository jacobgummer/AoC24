import numpy as np
import sys
import heapq

file = ''

DIRS = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
OPPOSITE = {'^': 'v', 'v': '^', '<': '>', '>': '<'}
TURN = {'^': ['<', '>'], 'v': ['<', '>'], '<': ['^', 'v'], '>': ['^', 'v']}

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

DIRS = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}

def parse_lines(lines: list[str]) -> np.ndarray:
    rows = []
    start_pos = (0,0)
    for i, line in enumerate(lines):
        rows.append([c for c in line])
        if 'S' in line:
            start_pos = (i, line.index('S'))
        if 'E' in line:
            end_pos = (i, line.index('E'))
    return np.array(rows), start_pos, end_pos

def is_valid(p, maze):
    i, j = p
    m, n = maze.shape
    return 0 <= i < m and 0 <= j < n and maze[p] != '#'

def get_neighbours(vertex: tuple[int, int]):
    return [(vertex[0] + dx, vertex[1] + dy) for dx, dy in DIRS.values()]
    
    
def dijkstra(maze: np.ndarray, start_pos: tuple[int, int], end_pos: tuple[int, int]):
    pq = []
    visited = set()
    
    heapq.heappush(pq, (0, start_pos, '>'))
    path = []

    while pq:
        cost, p, direction = heapq.heappop(pq)
        
        if (p, direction) in visited:
            continue
        visited.add((p, direction))
        
        if p == end_pos:
            return cost
        
        neighbours = {k: n for k, n in zip(DIRS.keys(), get_neighbours(p))
                        if is_valid(n, maze)}
        
        for new_dir, next_p in neighbours.items():
            new_cost = 1001 if new_dir != direction else 1
            heapq.heappush(pq, (new_cost + cost, next_p, new_dir))
        
maze, start, end = parse_lines(lines)
least = dijkstra(maze, start, end)
print(least)