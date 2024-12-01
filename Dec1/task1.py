import numpy as np

input = open('./input.txt', 'r')
lines = input.read().splitlines()
input.close()

fst, snd = [], []
for line in lines:
    nums = [int(x) for x in line.split()]
    fst.append(nums[0])
    snd.append(nums[1])

fst, snd = np.array(sorted(fst)), np.array(sorted(snd))
res = np.sum(np.abs(fst - snd))
print(res)