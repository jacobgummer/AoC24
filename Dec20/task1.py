import sys
import numpy as np
import heapq
from copy import deepcopy
from itertools import combinations

file = ''
DIRS = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1),}

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

def parse_lines(lines):
    racetrack = []
    for line in lines:
        racetrack.append([c for c in line])
    return racetrack

def get_start_and_end(racetrack: list[str]):
    start = (0,0)
    end = (0,0)
    for i, line in enumerate(racetrack):
        if 'S' in line:
            start = i, line.index('S')
        if 'E' in line:
            end = i, line.index('E')
    return start, end
        
def is_valid(p, shape, racetrack):
    i, j = p
    m, n = shape
    return 0 <= i < m and 0 <= j < n and (racetrack[i][j] == '.' or racetrack[i][j] == 'E')

def are_both_on_track(points, racetrack):
    (i1, j1), (i2, j2) = points
    return ((racetrack[i1][j1] == '.' or racetrack[i1][j1] == 'E' or racetrack[i1][j1] == 'S') 
            and (racetrack[i2][j2] == '.' or racetrack[i2][j2] == 'E' or racetrack[i1][j1] == 'S'))

def get_neighbours(tile: tuple[int, int]):
    return [(tile[0] + dx, tile[1] + dy) for dx, dy in DIRS.values()]

def get_walls(racetrack):
    wall_positions = []
    for i in range(1, len(racetrack) - 1):
        for j in range(1, len(racetrack[0]) - 1):
            if racetrack[i][j] == '#':
                p = (i, j)
                around = get_neighbours(p)
                if are_both_on_track(around[:2], racetrack) or are_both_on_track(around[2:], racetrack):
                    wall_positions.append(p)
    return wall_positions

def dijkstra(racetrack, start_pos: tuple[int, int], end_pos, shape):
    pq = []
    dist = {start_pos: 0}
    
    heapq.heappush(pq, (0, start_pos))
    while pq:
        _, u = heapq.heappop(pq)
        if u == end_pos:
            return dist
            
        neighbours = [n for n in get_neighbours(u) if is_valid(n, shape, racetrack)]
        for v in neighbours:
            alt = dist[u] + 1
            if alt < dist.get(v, float('inf')):
                dist[v] = alt
                heapq.heappush(pq, (alt, v))

def check_cheats(racetrack, start, end, wall_positions):
    best_dists = dict()
    shape = (len(racetrack), len(racetrack[0]))
    
    no_cheat_dists = dijkstra(racetrack, start, end, shape)
    best_no_cheat = no_cheat_dists[end]
    
    possible = 0
    
    combs = combinations(no_cheat_dists.items(), 2)
    for (p1, d1), (p2, d2) in combs:
        manh_dist = abs((p1[0] - p2[0])) + abs((p1[1] - p2[1]))
        if manh_dist == 2:
            saved = abs(d2 - d1) - manh_dist
            if saved >= 100:
                possible += 1
    
    print(possible)


def draw(racetrack: list[list[str]], wall_positions):
    r_copy = deepcopy(racetrack)
    for x, y in wall_positions:
        r_copy[x][y] = 'O'
    for line in r_copy:
        print(line)

racetrack = parse_lines(lines)
wall_positions = get_walls(racetrack)

start, end = get_start_and_end(racetrack)
shape = (len(racetrack), len(racetrack[0]))
check_cheats(racetrack, start, end, wall_positions)
