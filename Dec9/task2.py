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
line = input.read().splitlines()[0]
input.close()

class Node:
    def __init__(self, id, length):
        self.id = id
        self.length = length
        self.next = None
        self.prev = None
    
    def __repr__(self):
        return f'[{self.id}, {self.length}]'

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

def front_append_linked_list(head: Node, id, length):
    new_node = Node(id, length)
    new_node.next = head
    if head:
        head.prev = new_node
    return new_node

def make_linked_list(file_lens: dict, free_space_dict: dict):
    ids_rev = list(file_lens.keys())[::-1]
    head = front_append_linked_list(None, ids_rev[0], file_lens[ids_rev[0]])
    for id in ids_rev[1:]:
        free_space = free_space_dict[id]
        if free_space != 0:
            head = front_append_linked_list(head, -id - 1, free_space)
        length = file_lens[id]
        head = front_append_linked_list(head, id, length)
    return head

def insert_before(head: Node, key, id, length):
    curr = head
    while curr:
        if curr.id == key:
            break
        curr = curr.next
    if not curr:
        return head

    new_node = Node(id, length)
    new_node.prev = curr.prev
    new_node.next = curr
    
    if curr.prev:
        curr.prev.next = new_node
    else:
        head = new_node

    curr.prev = new_node

    return head

def traverse(head: Node):
    current = head
    s = []
    while current:
        if current.id >= 0:
            s += [current.id] * current.length
        else:
            s += [0] * current.length
        current = current.next
    return s

def get_node_with_id(head: Node, id: int):
    node = head
    while node and node.id != id:
        node = node.next
    return node

def find_free_space(head: Node, space_needed, curr_id):
    node = head
    while node and node.id != curr_id and (node.id >= 0 or node.length < space_needed):
        node = node.next
        
    if node.id == curr_id: 
        return None
    return node

def del_id(head: Node, key: int):
    curr = head

    while curr:
        if curr.id == key:
            break
        curr = curr.next
        
    assert curr
    
    if curr.prev:
        curr.prev.next = curr.next

    if curr.next:
        curr.next.prev = curr.prev

    if head == curr:
        head = curr.next
    
    return head

def merge_free_blocks(head: Node):
    node = head
    while node and node.next:
        if node.id < 0 and node.next.id < 0:
            node.length += node.next.length
            node.next = node.next.next
        node = node.next
    return head

def alter_layout(file_lens: dict, free_space_dict: dict):
    head = make_linked_list(file_lens, free_space_dict)
    ids = list(file_lens.keys())
    for id in ids[::-1][:-1]:
        node = get_node_with_id(head, id)
        
        free_block = find_free_space(head, node.length, id)
        if not free_block:
            continue
        head = insert_before(head, free_block.id, node.id, node.length)
        
        new_free_space = node.length - free_block.length
        if new_free_space == 0:
            head = del_id(head, free_block.id)
        else: 
            free_block.length -= node.length
            
        node.id = -100000 - id
        head = merge_free_blocks(head)
    return traverse(head)

def checksum(new_layout):
    s = 0
    for i in range(len(new_layout)):
        s += i * new_layout[i]
    return s

layout, file_lens, free_space_dict = get_layout(line)
new_layout = alter_layout(file_lens, free_space_dict)
s = checksum(new_layout)
print(s)