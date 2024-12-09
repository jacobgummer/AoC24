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
line = input.read().splitlines()[0]
input.close()

def get_layout(line):
    n = len(line)
    id = 0
    file_lens = dict()
    free_space_dict = dict()
    layout = []
    for i in range(n // 2 + 1):
        if i != n // 2:
            len_file, free_space = int(line[i * 2]), int(line[i * 2 + 1])
            layout += [id] * len_file
            layout += ['.'] * free_space
            file_lens[id] = len_file
            free_space_dict[id] = free_space
            id += 1
        else:
            len_file = int(line[-1])
            file_lens[id] = len_file
            layout += [id] * len_file
    return layout, file_lens, free_space_dict

def move(layout, file_lens: dict, free_space_dict: dict):
    n = len(layout)
    i, j = 0, n - 1
    while i < j:
        while layout[i] != '.':
            i += 1
        while layout[j] == '.':
            j -= 1
        while layout[i] == '.' and layout[j] != '.':
            layout[i] = layout[j]
            layout[j] = '.'
    layout[j] = layout[i]
    layout[i] = '.'
    return layout
    
def checksum(new_layout):
    s = 0
    for i in range(len(new_layout)):
        s += i * new_layout[i]
    return s

layout, file_lens, free_space_dict = get_layout(line)

new_layout = move(layout, file_lens, free_space_dict)
new_layout = new_layout[:new_layout.index('.')]

s = checksum(new_layout)
print(s)
