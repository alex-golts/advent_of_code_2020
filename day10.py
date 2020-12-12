import numpy as np

f = open('input10.txt','r')
txt = f.read()
txt = txt.split('\n')[:-1]
puzzle_input = [int(item) for item in txt]

vec = np.sort(np.array(puzzle_input))
diff_vec = np.diff(vec)

diff1 = (diff_vec==1).sum()+1
diff3 = (diff_vec==3).sum()+1
print(f'part 1 result = {diff1*diff3}')