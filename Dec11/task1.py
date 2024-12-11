import sys
import re
from time import time 

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
nums = input.read().split()
input.close()

PATTERN = r'^[^,]+,[^,]+$'

def blink(nums: list[str], cache: dict[str, str], blinked=25):
    if blinked == 0:
        return nums
    
    new_nums = []
    for n in nums:
        if not cache.get(n):
            if len(n) % 2 == 0:
                fst, snd = n[:len(n) // 2], str(int(n[len(n) // 2:]))
                new_nums.append(fst)
                new_nums.append(snd)
                cache[n] = f'{fst},{snd}'
            else:
                new = str(int(n) * 2024)
                new_nums.append(new)
                cache[n] = new
        else:
            transformation = cache[n]
            if re.match(PATTERN, transformation):
                l = transformation.split(',')
                new_nums.append(l[0])
                new_nums.append(l[1])
            else:
                new_nums.append(transformation) 
    
    return blink(new_nums, cache, blinked - 1)

cached_transformations = {}
cached_transformations['0'] = '1'

start = time()
transformed = blink(nums, cached_transformations)
end = time()
print(len(transformed))
print(f'Runtime: {(end - start) * 10**3} ms')