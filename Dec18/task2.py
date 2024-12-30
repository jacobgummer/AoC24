import numpy as np
import sys
import heapq

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

DIRS = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}

def get_bytes(lines: list[str]) -> np.ndarray:
    bytes = []
    for line in lines:
        c = line.split(',')
        bytes.append((int(c[1]), int(c[0])))
    return bytes

def is_valid(p, shape, bytes):
    i, j = p
    m, n = shape
    return 0 <= i < m and 0 <= j < n and p not in bytes

def get_neighbours(vertex: tuple[int, int]):
    return [(vertex[0] + dx, vertex[1] + dy) for dx, dy in DIRS.values()]
    
    
def dijkstra(bytes: list[tuple[int,int]], shape, start_pos: tuple[int, int], num_fallen: int):
    fallen_bytes = bytes[:num_fallen]
    pq = []
    dist = {start_pos: 0}
    
    heapq.heappush(pq, (0, start_pos))

    while pq:
        _, u = heapq.heappop(pq)
        neighbours = [n for n in get_neighbours(u) if is_valid(n, shape, fallen_bytes)]
        for v in neighbours:
            alt = dist[u] + 1
            if alt < dist.get(v, float('inf')):
                dist[v] = alt
                heapq.heappush(pq, (alt, v))
                
    return dist

def print_map(bytes_fallen, shape):
    grid = [['.' for _ in range(shape[1] + 1)] for _ in range(shape[0] + 1)]
    for i, j in bytes_fallen:
        grid[i][j] = '#'
    print(np.array(grid))

bytes = get_bytes(lines)
shape = (71, 71)
dist = dijkstra(bytes, shape, (0,0), 2862)