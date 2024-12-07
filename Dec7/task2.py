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

def equation_holds(result, equation):
    if len(equation) == 1:
        return equation[0] == result
    
    if equation_holds(result, [equation[0] + equation[1]] + equation[2:]):
        return True
    if equation_holds(result, [equation[0] * equation[1]] + equation[2:]):
        return True
    if equation_holds(result, [int(str(equation[0]) + str(equation[1]))] + equation[2:]):
        return True

def check_all(results, equations):
    total = 0
    for res, eq in zip(results, equations):
        total += res if equation_holds(res, eq) else 0
    return total

results, equations = [], []
for line in lines:
    res, eq = line.split(':')
    results.append(int(res))
    equations.append([int(n) for n in eq.strip().split(' ')])

total = check_all(results, equations)
print(total)