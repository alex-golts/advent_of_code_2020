start_list = [14,1,17,0,3,20]
last_turn = 2020

def first_occasion(lst, num):
    for i,v in enumerate(lst):
        if v==num:
            return i

num_list = start_list.copy()
for i in range(len(num_list)+1,last_turn+1):
    last_spoken = num_list[-1]
    if last_spoken not in num_list[:-1]:
        next_num = 0
    else:
        next_num = first_occasion(num_list[:-1][::-1], last_spoken)+1
    num_list.append(next_num)
    
print(f'part 1 result = {num_list[-1]}')

# part 2 
# now use a dictionary. for each spoken number store in its 
# corresponding key, the last time it was spoken
num_list = start_list.copy()
last_turn = 30000000

# initialize dict:
num_dict_prev = {}
for i,num in enumerate(num_list[:-1]):
    num_dict_prev[num] = i+1
last_spoken = num_list[-1]

for i in range(len(num_list)+1,last_turn+1):
    prev_spoken = last_spoken
    if last_spoken not in num_dict_prev:
        last_spoken = 0
    else:
        last_spoken = i-1-num_dict_prev[last_spoken]
    num_dict_prev[prev_spoken] = i-1    

print(f'part 2 answer = {last_spoken}')