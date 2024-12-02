input = open('./test.txt', 'r')
lines = input.read().splitlines()
input.close()

for i in range(len(lines)):
    lines[i] = [int(x) for x in lines[i].split()]

def analyze_report(report):
    n = len(report)
    fst_diff = report[1] - report[0]
    if fst_diff >= -3 and fst_diff <= -1: # decreasing
        for i in range(1, n-1):
            diff = report[i+1] - report[i]
            if diff < -3 or diff > -1: return 0
        return 1
    elif fst_diff >= 1 and fst_diff <= 3: # increasing
        for i in range(1, n-1):
            diff = report[i+1] - report[i]
            if diff < 1 or diff > 3: return 0
        return 1        
    return 0

safe_reports = 0
for report in lines:
    safe = analyze_report(report)
    if safe == 1: print(f'{report}')
    safe_reports += safe
    
print(safe_reports)