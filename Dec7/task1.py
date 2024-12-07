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

def is_valid(result, equation, curr_val):
    if len(equation) == 1:
        mul = curr_val * equation[0]
        sum = curr_val + equation[0]
        return mul == result or sum == result
    
    if is_valid(result, equation[1:], curr_val + equation[0]):
        return True
    if is_valid(result, equation[1:], curr_val * equation[0]):
        return True
    if is_valid(result, equation[1:], curr_val * equation[0]):
        return True

def check_all(results, equations):
    total = 0
    for res, eq in zip(results, equations):
        total += res if is_valid(res, eq[1:], eq[0]) else 0
    return total

results, equations = [], []
for line in lines:
    res, eq = line.split(':')
    results.append(int(res))
    equations.append([int(n) for n in eq.strip().split(' ')])

total = check_all(results, equations)
print(total)