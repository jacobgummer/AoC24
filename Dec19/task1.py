import numpy as np
import sys
from functools import cmp_to_key

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
    split = lines.index('')
    
    available = lines[:split][0].split(', ')
    available.sort(key=lambda x: (-len(x), x))
    
    needed = lines[split+1:]
    return available, needed

def check_one(available, towel, n):
    if n == 0:
        return 1

    for a in available:
        a_n = len(a)
        if a_n <= n and towel[:a_n] == a and check_one(available, towel[a_n:], n - a_n):
            return 1
    return 0

def check_all(available, needed):
    possible = 0
    for towel in needed:
        possible += check_one(available, towel, len(towel))
    return possible

available, needed = parse_lines(lines)
print(available)
print(needed)
print()

possible = check_all(available, needed)
print(possible)