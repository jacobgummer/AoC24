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

def get_safety_factor(positions, velocities, shape):
    test_map = np.zeros(shape)
    new_positions = (positions + 100 * velocities) % shape
    for p in new_positions:
        if test_map[p[0], p[1]] != 0:
            test_map[p[0], p[1]] += 1
        else:
            test_map[p[0], p[1]] = 1

    m, n = test_map.shape
    prod = 1
    prod *= np.sum(test_map[:m // 2, :n // 2])
    prod *= np.sum(test_map[:m // 2, n // 2 + 1:])
    prod *= np.sum(test_map[m // 2 + 1:, :n // 2])
    prod *= np.sum(test_map[m // 2 + 1:, n // 2 + 1:])
    
    return int(prod)
        
positions, velocities = parse_lines(lines)
positions, velocities = np.array(positions), np.array(velocities)

test_p, test_v = positions[10], velocities[10]
new_p = (test_p + 5 * test_v) % [7, 11]

safety_factor = get_safety_factor(positions, velocities, (103, 101))
print(safety_factor)