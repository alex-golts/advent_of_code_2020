f = open('input5.txt','r')
txt = f.read()
txt = txt.split('\n')
puzzle_input = txt

def rowstr2num(s):
    s = s.replace('F','0')
    s = s.replace('B','1')
    return s

def colstr2num(s):
    s = s.replace('L','0')
    s = s.replace('R','1')
    return s

ids = [8*int(rowstr2num(item[:-3]),2) + int(colstr2num(item[-3:]),2) for item in puzzle_input]

print(f'part 1 answer = {max(ids)}')

# part 2:
ids = sorted(ids)
prev_id = ids[0]
for item in ids:
    if item-prev_id>1:
        my_id = item-1
        break
    prev_id = item

print(f'part 2 answer = {my_id}')