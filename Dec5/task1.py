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
lines = input.read().splitlines()
input.close()

def build_rules(rules: list[str]):
    dict = {}
    for rule in rules:
        fst, snd = rule.split('|')
        fst, snd = int(fst), int(snd)
        if not dict.get(fst):
            dict[fst] = []
        dict[fst].append(snd)
    return dict

nl = lines.index('')
rules, updates = lines[:nl], lines[nl + 1:]
updates = [x.split(',') for x in updates]
for i, lst in enumerate(updates):
    updates[i] = [int(x) for x in lst]

dict = build_rules(rules)

def check_updates(updates, dict):
    total = 0
    for update in updates:
        total += check_update(update, dict)
    return total
    
def check_update(update, dict):
    printed = [update[0]]
    for n in update[1:]:
        if not printed_vs_update(printed, n, dict): return 0
        printed.append(n)
    return update[len(update) // 2]
    
def printed_vs_update(printed, n, dict):
    for p in printed:
        if dict.get(n) and p in dict[n]: return False
    return True
   
total = check_updates(updates, dict)
print(total)