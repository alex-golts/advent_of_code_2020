#num_list = [0,3,6]
num_list = [14,1,17,0,3,20]
last_turn = 2020
#last_turn = 30000000

def first_occasion(lst, num):
    for i,v in enumerate(lst):
        if v==num:
            return i
        
for i in range(len(num_list)+1,last_turn+1):
    last_spoken = num_list[-1]
    if last_spoken not in num_list[:-1]:
        next_num = 0
    else:
        next_num = first_occasion(num_list[:-1][::-1], last_spoken)+1
    num_list.append(next_num)
    
print(f'part 1 result = {num_list[-1]}')