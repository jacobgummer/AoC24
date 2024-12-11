import sys
import re

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

def blink(nums: dict[str, int], blinked=75):
    if blinked == 0:
        return nums
    
    new_nums = {'0': 0}
    for k in nums:
        if k == '0':
            new_nums['1'] = nums[k]
        elif len(k) % 2 == 0:
            fst, snd = k[:len(k) // 2], str(int(k[len(k) // 2:]))
            if not new_nums.get(fst):
                new_nums[fst] = 0
            if not new_nums.get(snd):
                new_nums[snd] = 0
            new_nums[fst] += nums[k]
            new_nums[snd] += nums[k]
        else:
            new_stone = str(int(k) * 2024)
            if not new_nums.get(new_stone):
                new_nums[new_stone] = 0
            new_nums[new_stone] += nums[k]
            
    return blink(new_nums, blinked - 1)

nums = {k:1 for k in nums}
if not nums.get('0'):
    nums['0'] = 0
nums = dict(sorted(nums.items()))

transformed = blink(nums)
print(sum(list(transformed.values())))