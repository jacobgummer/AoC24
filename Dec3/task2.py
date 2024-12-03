import numpy as np
import re
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
lines = input.read()
input.close()

regex = r'(mul\([0-9]+,[0-9]+\)|do(?!n\'t)|don\'t)'
check = re.findall(regex, lines)

final_muls = []
def DO(matches, i, n):
    while i < n and matches[i] != "don\'t":
        # print(f'matches[i] = {matches[i]} ({matches[i] != "don\'t"})')
        if matches[i] != 'do': final_muls.append(matches[i])
        i += 1
    if i < n - 1: DONT(matches, i + 1, n)
        
def DONT(matches, i, n):
    while i < n and matches[i] != 'do':
        i += 1
    if i < n - 1: DO(matches, i + 1, n)
    
DO(check, 0, len(check))
regex2 = r'(?<=\()[0-9]+(?=,)'
regex3 = r'(?<=,)[0-9]+'

arr1 = np.array([int(x) for x in [re.findall(regex2, match)[0] for match in final_muls]])
arr2 = np.array([int(x) for x in [re.findall(regex3, match)[0] for match in final_muls]])
print(np.sum(arr1 * arr2))
        