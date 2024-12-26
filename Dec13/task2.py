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

def get_eq(button: str):
    fst, snd = button.split(',')
    _, X = fst.split('+')
    _, Y = snd.split('+')
    return np.array([int(X), int(Y)])

def get_prize(s: str):
    fst, snd = s.split(',')
    _, X = fst.split('=')
    _, Y = snd.split('=')
    return np.array([int(X), int(Y)])

def format(lines):
    all_systems = []
    j = 0
    for i in range(0, len(lines), 4):
        all_systems.append(dict())
        
        _, but_A = lines[i].split(':')
        but_A = get_eq(but_A)
        
        _, but_B = lines[i+1].split(':')
        but_B = get_eq(but_B)
        
        _, s = lines[i+2].split(':')
        prize = get_prize(s)
        
        all_systems[j] = {'A': but_A, 'B': but_B, 'prize': prize}
        j += 1
        
    return all_systems

def check_systems(all_systems: list[dict[str, np.ndarray]]):
    total_tokens = 0
    for system in all_systems:
        total_tokens += check_system(system)
    return total_tokens

def check_system(system: dict[str, np.ndarray]):
    A = system['A']
    B = system['B']
    P = system['prize'].reshape((2, 1)) + 10000000000000
    
    mat_A = np.hstack((A.reshape((1, 2)).T, B.reshape((1, 2)).T))
        
    x = np.round(np.linalg.solve(mat_A, P))
    tokens = int((np.array([3, 1]) @ x)[0])
    check = np.array_equal(mat_A @ x, P)
    return tokens if np.array_equal(mat_A @ x, P) else 0

all_systems = format(lines)

tokens_needed = check_systems(all_systems)
print(tokens_needed)
