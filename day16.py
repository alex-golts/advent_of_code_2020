import numpy as np

f = open('input16.txt','r')
txt = f.read()
puzzle_input = txt.split('\n')


my_ticket_line = puzzle_input.index('your ticket:')
nearby_tickets_line = puzzle_input.index('nearby tickets:')

def parse_field_line(line):
    line2 = line.replace('-',' ')
    numbers = [int(item) for item in line2.split() if item.isdigit()]
    fieldname = line2.split(':')[0]
    return fieldname, [[numbers[0], numbers[1]], [numbers[2], numbers[3]]]

fieldnames = []
valid_ranges = []
for i,line in enumerate(puzzle_input[:my_ticket_line-1]):
    fieldname,ranges = parse_field_line(line)
    valid_ranges.append(ranges[0])
    valid_ranges.append(ranges[1])
    fieldnames.append(fieldname)

nearby_nums = []
for i,line in enumerate(puzzle_input[nearby_tickets_line+1:]):
    nearby_nums += [int(item) for item in line.split(',')]

def valid_num(num, valid_ranges):
    return sum([num>=item[0] and num<=item[1] for item in valid_ranges])>0

bad_nums = [item for item in nearby_nums if not valid_num(item, valid_ranges)]
print(f'part 1 result = {sum(bad_nums)}')

# part 2
nearby_tickets = []
for i,line in enumerate(puzzle_input[nearby_tickets_line+1:]):
    nearby_tickets.append([int(item) for item in line.split(',')])

valid_nearby_tickets = []
for ticket in nearby_tickets:
    if sum([not valid_num(item, valid_ranges) for item in ticket])>0:
        continue
    else:
        valid_nearby_tickets.append(ticket)

# convert ranges to be the same length as fieldnames with corresponding indices
valid_ranges_2 = list(map(list, zip(valid_ranges[::2], valid_ranges[1::2])))

# convert valid tickets to matrix:
def list2mat(lst):
    mat = np.zeros((len(lst), len(lst[0])))
    for i in range(len(lst)):
        for j in range(len(lst[0])):
            mat[i,j] = lst[i][j]
    return mat

valid_tickets_mat = list2mat(valid_nearby_tickets)

# for each column, go over all rows and check which field they all can belong to
correct_field = np.zeros((valid_tickets_mat.shape[1]))
can_belong = np.zeros((valid_tickets_mat.shape[0], valid_tickets_mat.shape[1], valid_tickets_mat.shape[1]))

for i in range(valid_tickets_mat.shape[0]):
    for j in range(valid_tickets_mat.shape[1]):
        for k in range(len(valid_ranges_2)):
            if valid_num(valid_tickets_mat[i,j], valid_ranges_2[k]):
                can_belong[i,j,k] = 1

row_count_mat = np.sum(can_belong,0)

max_vec = np.argwhere(row_count_mat==np.max(row_count_mat,1))

# find a field that occurs only once, assign it and then remove and continue:
field_map = np.zeros((valid_tickets_mat.shape[1]))
lst = list(max_vec[:,0])
lst2 = list(max_vec[:,1])
found_sources = []
found_targets = []

while True:
    # ugly solution but it works...
    if len(lst)==0:
        break
    row = [x for x in lst if lst.count(x)==1]
    ind = lst.index(row[0])
    field_map[row[0]] = lst2[ind]
    source_val = row[0]
    target_val = lst2[ind]
    can_belong[:, source_val, :] = 0
    can_belong[:, source_val, target_val] = 1
    row_count_mat = np.sum(can_belong,0)
    max_vec = np.argwhere(row_count_mat==np.max(row_count_mat,1))
    inds2 = [i for i,item in enumerate(lst2) if item==target_val]
    lst = [item for i,item in enumerate(lst) if i not in list(inds2)]
    lst2 = [item for i,item in enumerate(lst2) if i not in list(inds2)]

my_ticket = [int(item) for item in puzzle_input[my_ticket_line+1].split(',')]
inds = [i for i,item in enumerate(fieldnames) if item.startswith('departure')]
vals = [int(item) for i,item in enumerate(my_ticket) if field_map[i] in inds]

def product(list):
    p = 1
    for i in list:
        p *= i
    return p

mult_vals = product(vals)
print(f'part 2 result = {mult_vals}')