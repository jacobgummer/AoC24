import numpy as np
import sys

file = ''

DIRS = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}

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

def convert_to_2d(lines: list[str]) -> np.ndarray:
    rows = []
    for line in lines:
        rows.append([c for c in line])
    return np.array(rows)

def resize(lines):
    new_lines = []
    for i in range(len(lines)):
        new_lines.append([])
        for j in range(len(lines[0])):
            curr = lines[i][j]
            if curr == '.':
                new_lines[i].append('.')
                new_lines[i].append('.')
            elif curr == '#':
                new_lines[i].append('#')
                new_lines[i].append('#')
            elif curr == 'O':
                new_lines[i].append('[')
                new_lines[i].append(']')
            elif curr == '@':
                new_lines[i].append('@')
                new_lines[i].append('.')
    
    return new_lines

def get_all_positions(lines: list[str]):
    start_pos = (0, 0)
    box_positions = []
    wall_positions = []
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            curr = lines[i][j]
            if curr == '[':
                box_positions.append([i, j, i, j + 1])
                j += 1
            elif curr == '#':
                wall_positions.append([i, j])
            elif curr == '@':
                start_pos = np.asarray((i, j))

    return start_pos, np.array(box_positions), np.array(wall_positions)

def check(positions, to_check):
    return np.where((positions == to_check).all(axis = 1))[0]

def can_move_check(curr_pos, move, box_positions, wall_positions):
    new_pos = curr_pos + DIRS[move] * 2
    new_box_positions = np.delete(box_positions, check(box_positions, curr_pos)[0], axis = 0)
    left_new, right_new = new_pos[:2], new_pos[2:]
    left_all, right_all = new_box_positions[:, :2], new_box_positions[:, 2:]
    
    # Crash with wall
    if len(check(wall_positions, left_new)) > 0 or len(check(wall_positions, right_new)) > 0:
        return False
    
    r_l_box_crash = check(right_all, left_new)
    l_r_box_crash = check(left_all, right_new)
    l_l_box_crash = check(left_all, left_new)
    l1, l2, l3 = len(r_l_box_crash), len(l_r_box_crash), len(l_l_box_crash)
    if l1 and l2:
        left_box_pos = new_box_positions[r_l_box_crash[0]]
        check1 = can_move_check(left_box_pos, move, new_box_positions, wall_positions)
        if check1:
            right_box_pos = new_box_positions[l_r_box_crash[0]]
            check2 = can_move_check(right_box_pos, move, new_box_positions, wall_positions)
        return check1 and check2

    # Crash with one box
    elif l1: # r_l
        next_box_pos = new_box_positions[r_l_box_crash[0]]
        return can_move_check(next_box_pos, move, new_box_positions, wall_positions) 
        
    elif l2: # l_r
        next_box_pos = new_box_positions[l_r_box_crash[0]]
        return can_move_check(next_box_pos, move, new_box_positions, wall_positions)
    
    elif l3: # l_l
        next_box_pos = new_box_positions[l_l_box_crash[0]]
        return can_move_check(next_box_pos, move, new_box_positions, wall_positions)
    
    return True

def move_boxes(curr_pos, move, box_positions: np.ndarray):
    to_be_moved = []
    if tuple(curr_pos) not in to_be_moved:
        to_be_moved.append(tuple(curr_pos))
    
    new_pos = curr_pos + DIRS[move] * 2
    left_new, right_new = new_pos[:2], new_pos[2:]

    new_box_positions = np.delete(box_positions, check(box_positions, curr_pos)[0], axis=0)
    
    left_all, right_all = new_box_positions[:, :2], new_box_positions[:, 2:]
    
    r_l_box_crash = check(right_all, left_new)
    l_r_box_crash = check(left_all, right_new)
    l_l_box_crash = check(left_all, left_new)
    l1, l2, l3 = len(r_l_box_crash), len(l_r_box_crash), len(l_l_box_crash)
    if l1:
        next_pos = new_box_positions[r_l_box_crash[0]]
        to_be_moved = list(set(to_be_moved).union(move_boxes(next_pos, move, new_box_positions)))
    if l2:
        next_pos = new_box_positions[l_r_box_crash[0]]
        to_be_moved = list(set(to_be_moved).union(move_boxes(next_pos, move, new_box_positions)))
        
    if l3:
        next_pos = new_box_positions[l_l_box_crash[0]]
        to_be_moved = list(set(to_be_moved).union(move_boxes(next_pos, move, new_box_positions)))

    return to_be_moved


def move_robot(lines: list[str], moveset: str):
    start_pos, box_positions, wall_positions = get_all_positions(lines)
    m, n = len(lines), len(lines[0])
    
    curr_pos = start_pos
    for move in moveset:
        can_move = True
        new_pos = curr_pos + DIRS[move]
        box_pos = None
        wall_crash_indices = np.where((wall_positions == new_pos).all(axis = 1))[0]
        if len(wall_crash_indices) > 0:
            continue
        
        left_box_crash_indices = np.where((box_positions[:,:2] == new_pos).all(axis = 1))[0]
        if len(left_box_crash_indices) > 0:
            i = left_box_crash_indices[0]
            box_pos = box_positions[i]
            can_move = can_move_check(box_pos, move, box_positions, wall_positions)
            
        right_box_crash_indices = np.where((box_positions[:,2:] == new_pos).all(axis = 1))[0]
        if len(right_box_crash_indices) > 0:
            i = right_box_crash_indices[0]
            box_pos = box_positions[i]
            can_move = can_move_check(box_pos, move, box_positions, wall_positions)
        
        if can_move:
            if box_pos is not None:
                to_be_moved = move_boxes(box_pos, move, box_positions)
                
                to_be = []
                for bp in to_be_moved:
                    to_be.append(np.asarray(bp))
                to_be = np.array(to_be)
                
                for row in to_be:
                    idxs = check(box_positions, row)
                    box_positions[idxs[0]] = box_positions[idxs[0]] + 2 * DIRS[move]
            curr_pos = new_pos
            
    return curr_pos, box_positions

def draw_new(shape, box_positions, wall_positions, start_pos):
    new = []
    for i in range(shape[0]):
        new.append([])
        for j in range(shape[1]):
            is_left_box = check(box_positions[:, :2], np.asarray((i, j)))
            is_right_box = check(box_positions[:, 2:], np.asarray((i, j)))
            is_wall = check(wall_positions, np.asarray((i, j)))
            if len(is_left_box):
                new[i].append('[')
            elif len(is_right_box):
                new[i].append(']')
            elif len(is_wall):
                new[i].append('#')
            elif tuple(start_pos) == (i, j):
                new[i].append('@')
            else:
                new[i].append('.')
                
    return np.array(new)

def write_new_to_file(new_map: np.ndarray, text: str):
    s = [text, '\n']
    for i in range(new_map.shape[0]):
        for j in range(new_map.shape[1]):
            s.append(new_map[i, j])
        s.append('\n')
    s.append('\n')
    with open('checking.txt', 'a') as f:
        f.write(''.join(s))
        
write_file = ''
lines, moveset = lines[:lines.index('')], ''.join(lines[lines.index('') + 1:])
resized = resize(lines)
write_new_to_file(np.array(resized), 'Initial:')

start_pos, box_positions, wall_positions = get_all_positions(resized)
final_pos, box_positions = move_robot(resized, moveset)
box_positions = box_positions[np.lexsort(box_positions.T[::-1])]

m, n = len(resized), len(resized[0])
new_map = draw_new((m, n), box_positions, wall_positions, final_pos)
write_new_to_file(new_map, 'Final:')


GPS_coords = box_positions[:, :2] @ np.array([100, 1]).reshape((2, 1))
print(np.sum(GPS_coords))