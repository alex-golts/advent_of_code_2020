import numpy as np

f = open('input3.txt','r')
txt = f.read()
txt = txt.split('\n')
puzzle_input = txt

def list2mat(lst):
    mat = np.zeros((len(lst), len(lst[0])))
    for i in range(len(lst)):
        for j in range(len(lst[0])):
            if lst[i][j] == '.':
                mat[i,j] = 0
            elif lst[i][j] == '#':
                mat[i,j] = 1
    return mat

input_mat = list2mat(puzzle_input)

# duplicate from the right till the number of columns is 3x the number of rows:
input_mat_large = np.tile(input_mat, (1, int(np.ceil(3*(input_mat.shape[0]/input_mat.shape[1])))))

# go down slope and count trees:
def go_down_slope(input_mat, slope_xy):
    x_pos = 0
    y_pos = 0
    cnt_trees = 0
    while y_pos<input_mat.shape[0]-1:
        x_pos += slope_xy[0]
        y_pos += slope_xy[1]
        if input_mat[y_pos, x_pos]==1:
            cnt_trees+=1
    return cnt_trees


res1 = go_down_slope(input_mat_large, [3,1])
print(f'part 1 result = {res1}')


slope_list = [[1,1],[3,1],[5,1],[7,1],[1,2]]

trees = np.zeros((len(slope_list)))
for ind,sl in enumerate(slope_list):
    input_mat_large = np.tile(input_mat, (1, int(np.ceil((sl[0]/sl[1])*(input_mat.shape[0]/input_mat.shape[1])))))

    trees[ind] = go_down_slope(input_mat_large, sl)

print(f'part 2 result = {int(np.prod(trees))}')
