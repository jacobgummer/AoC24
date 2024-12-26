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

def parse_lines(lines: list[str]):
    pos, vels = [], []
        
    for line in lines:
        fst, snd = line.split(' ')
        _, p = fst.split('=')
        p0, p1 = p.split(',')
        p = (int(p1), int(p0))
        
        _, v = snd.split('=')
        v0, v1 = v.split(',')
        v = (int(v1), int(v0))
        pos.append(p)
        vels.append(v)
        
    return pos, vels

def draw_map(map, i):
    with open('map.txt', 'a') as f:
        f.write(f'i = {i}\n')
        for row in map:
            f.write(' '.join(row) + '\n')

def make_maps(positions: np.ndarray, velocities, shape):
    i = 1
    while True:
        map = [['.' for _ in range(shape[1])] for _ in range(shape[0])]
        new_positions = (positions + i * velocities) % shape
        seen = set()
        is_tree = True
        for p in new_positions:
            if seen.isdisjoint([tuple(p)]):
                seen.add(tuple(p))
            else:
                is_tree = False
                break
        if is_tree:
            for p in new_positions:
                map[p[0]][p[1]] = 'x'
            draw_map(map, i)
            break
        i += 1
        
        
positions, velocities = parse_lines(lines)
positions, velocities = np.array(positions), np.array(velocities)
make_maps(positions, velocities, (103, 101))