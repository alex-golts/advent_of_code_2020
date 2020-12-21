f = open('input16.txt','r')
txt = f.read()
puzzle_input = txt.split('\n')


my_ticket_line = puzzle_input.index('your ticket:')
nearby_tickets_line = puzzle_input.index('nearby tickets:')

def parse_field_line(line):
    line2 = line.replace('-',' ')
    numbers = [int(item) for item in line2.split() if item.isdigit()]
    return [numbers[0], numbers[1]], [numbers[2], numbers[3]]

valid_ranges = []
for i,line in enumerate(puzzle_input[:my_ticket_line-1]):
    range1,range2 = parse_field_line(line)
    valid_ranges.append(range1)
    valid_ranges.append(range2)

nearby_nums = []
for i,line in enumerate(puzzle_input[nearby_tickets_line+1:]):
    nearby_nums += [int(item) for item in line.split(',')]

def valid_num(num, valid_ranges):
    return sum([num>=item[0] and num<=item[1] for item in valid_ranges])>0

bad_nums = [item for item in nearby_nums if not valid_num(item, valid_ranges)]
print(f'part 1 result = {sum(bad_nums)}')
