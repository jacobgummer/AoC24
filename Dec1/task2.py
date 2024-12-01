import numpy as np

input = open('./input.txt', 'r')
lines = input.read().splitlines()
input.close()

fst, snd = [], []
snd_dic = {}

for line in lines:
    nums = [int(x) for x in line.split()]
    n1 = nums[0]
    n2 = nums[1]
    
    if not snd_dic.get(n2):
        snd_dic[n2] = 1
    else:
        snd_dic[n2] += 1
        
    if not snd_dic.get(n1):
        snd_dic[n1] = 0
    
    fst.append(nums[0])

sim_lst = [x * snd_dic[x] for x in fst]

res = sum(sim_lst)
print(res)