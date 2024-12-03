import numpy as np
import re
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
lines = input.read()
input.close()

regex1 = r'mul\([0-9]+,[0-9]+\)'
test = [re.findall(regex1, line) for line in lines]
test = re.findall(regex1, lines)

regex2 = r'[0-9]+(?=,)'
regex3 = r'(?<=,)[0-9]+'

arr1 = np.array([int(x) for x in [re.findall(regex2, match)[0] for match in test]])
arr2 = np.array([int(x) for x in [re.findall(regex3, match)[0] for match in test]])
print(np.sum(arr1 * arr2))