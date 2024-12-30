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
    split = lines.index('')
    
    available = lines[:split][0].split(', ')
    
    needed = lines[split+1:]
    return available, needed

def check_one(available, towel, n, DP):
    if n == 0:
        return 1
    
    if towel in DP:
        return DP[towel]

    possible = 0
    for a in available:
        a_n = len(a)
        if a_n <= n and towel[:a_n] == a:
            possible += check_one(available, towel[a_n:], n - a_n, DP)
            
    DP[towel] = possible
    return possible

def check_all(available, needed):
    possible = 0
    DP = {'': 1}
    for towel in needed:
        possible += check_one(available, towel, len(towel), DP)
    return possible

available, needed = parse_lines(lines)
possible = check_all(available, needed)
print(possible)