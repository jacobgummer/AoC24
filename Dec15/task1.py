import numpy as np
import sys

file = ''

DIRS = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}

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

def convert_to_2d(lines: list[str]) -> np.ndarray:
    rows = []
    for line in lines:
        rows.append([c for c in line])
    return np.array(rows)

def get_all_positions(lines: list[str]):
    start_pos = (0, 0)
    box_positions = []
    wall_positions = []
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            curr = lines[i][j]
            if curr == 'O':
                box_positions.append([i, j])
            elif curr == '@':
                start_pos = np.asarray((i, j))
            elif curr == '#':
                wall_positions.append([i, j])
    return start_pos, np.array(box_positions), np.array(wall_positions)

def move_box(curr_pos, move, box_positions, wall_positions):
    can_move = True
    new_box_pos = curr_pos + DIRS[move]
    wall_crash_indices = np.where((wall_positions == new_box_pos).all(axis = 1))[0]
    if len(wall_crash_indices) > 0:
        return False, box_positions
    
    box_crash_indices = np.where((box_positions == new_box_pos).all(axis = 1))[0]
    if len(box_crash_indices) > 0:
        can_move, box_positions = move_box(new_box_pos, move, box_positions, wall_positions)
    
    if can_move:
        old_pos_i = np.where((box_positions == curr_pos).all(axis = 1))[0]
        box_positions = np.delete(box_positions, old_pos_i, axis = 0)
        box_positions = np.vstack([box_positions, new_box_pos])
        return True, box_positions
    
    return False, box_positions

def move_robot(lines: list[str], moveset: str):
    start_pos, box_positions, wall_positions = get_all_positions(lines)
    
    curr_pos = start_pos
    for move in moveset:
        can_move = True
        new_pos = curr_pos + DIRS[move]
        wall_crash_indices = np.where((wall_positions == new_pos).all(axis = 1))[0]
        if len(wall_crash_indices) > 0:
            continue
        
        box_crash_indices = np.where((box_positions == new_pos).all(axis = 1))[0]
        if len(box_crash_indices) > 0:
            assert len(box_crash_indices) == 1
            i = box_crash_indices[0]
            box_pos = box_positions[i]
            can_move, box_positions = move_box(box_pos, move, box_positions, wall_positions)
        
        if can_move:
            curr_pos = new_pos
    
    return curr_pos, box_positions
        
lines, moveset = lines[:lines.index('')], ''.join(lines[lines.index('') + 1:])
final_pos, box_positions = move_robot(lines, moveset)

GPS_coords = box_positions @ np.array([100, 1]).reshape((2, 1))
print(np.sum(GPS_coords))