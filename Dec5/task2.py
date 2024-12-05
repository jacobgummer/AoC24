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

def build_rules(rules: list[str]):
    dict = {}
    for rule in rules:
        fst, snd = rule.split('|')
        fst, snd = int(fst), int(snd)
        if not dict.get(snd):
            dict[snd] = []
        dict[snd].append(fst)
    return dict

nl = lines.index('')
rules, updates = lines[:nl], lines[nl + 1:]
updates = [x.split(',') for x in updates]
for i, lst in enumerate(updates):
    updates[i] = [int(x) for x in lst]

dict = build_rules(rules)

def check_printed(updates, dict):
    total = 0
    for i, update in enumerate(updates):
        printed = update
        
        is_wrong_order = bubble(printed, dict)
        total = total + printed[len(update) // 2] if is_wrong_order else total
    return total

def bubble(printed, dict):
    n = len(printed)
    is_wrong_order = False
    for i in range(n):
        for j in range(n - i - 1):
            if dict.get(printed[j]) and printed[j+1] in dict.get(printed[j]):
                printed[j], printed[j+1] = printed[j+1], printed[j]
                is_wrong_order = True
                
    return is_wrong_order
              
res = check_printed(updates, dict)
print(res)