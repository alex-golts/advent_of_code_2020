import numpy as np

f = open('input13.txt','r')
txt = f.read()
txt = txt.split('\n')
earliest_timestamp = int(txt[0])
busses = [int(item) for item in txt[1].split(',') if item!='x']
earliest_depart = [np.ceil(earliest_timestamp/busID)*busID for busID in busses]

ind = np.argmin(np.array(earliest_depart))

print(f'part 1 result = {int((earliest_depart[ind] - earliest_timestamp)*busses[ind])}')

# part 2:
# go over all numbers to find a least common multiplier of K bus IDs. 
# Begin with 1 bus, then 2 with steps bus[0], then 3 with step bus[1]*bus[2], 
# and so on.

deltas = [ind for ind,item in enumerate(txt[1].split(',')) if item!='x']

def product(list):
    p = 1
    for i in list:
        p *= i
    return p

cur_X = 100000000000000
cur_divisor_list = [busses[0]]
cur_X_delta = deltas[0]
delta_X = 1
cur_ind = 0
while True:
    cur_X += delta_X
    if (cur_X + cur_X_delta)%cur_divisor_list[-1]==0:
        cur_ind += 1 
        delta_X = product(cur_divisor_list)
        if cur_ind==len(busses):
            print(f'part 2 result = {cur_X}')
            break
        cur_X_delta = deltas[cur_ind]
        cur_divisor_list.append(busses[cur_ind])




