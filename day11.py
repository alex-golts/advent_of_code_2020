import numpy as np

f = open('input11.txt','r')
txt = f.read()
txt = txt.split('\n')
puzzle_input = txt

def map2mat(input_map):
    mat = np.zeros((len(input_map), len(input_map[0])))
    for i in range(len(input_map)):
        for j in range(len(input_map[0])):
            if input_map[i][j] == '.':
                mat[i][j] = 0
            elif input_map[i][j] == 'L':
                mat[i][j] = 1
            elif input_map[i][j] == '#':
                mat[i][j] = 2
    return mat

def occupied_adjacent(mat,i,j):
    top_left = int(mat[i-1,j-1]==2) if i>0 and j>0 else 0
    left = int(mat[i,j-1]==2) if j>0 else 0
    top_right = int(mat[i-1,j+1]==2) if i>0 and j<mat.shape[1]-1 else 0
    right = int(mat[i,j+1]==2) if j<mat.shape[1]-1 else 0
    up = int(mat[i-1,j]==2) if i>0 else 0
    down = int(mat[i+1,j]==2) if i<mat.shape[0]-1 else 0
    bottom_left = int(mat[i+1,j-1]==2) if i<mat.shape[0]-1 and j>0 else 0
    bottom_right = int(mat[i+1,j+1]==2) if i<mat.shape[0]-1 and j<mat.shape[1]-1 else 0

    return top_left + left + bottom_left + down + up + top_right + right + bottom_right

def evolve(mat):
    mat_new = mat.copy()
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            if mat[i,j] == 1 and occupied_adjacent(mat, i, j) == 0:
                mat_new[i,j] = 2
            if mat[i,j] == 2 and occupied_adjacent(mat, i, j)>=4:
                mat_new[i,j] = 1

    return mat_new

def has_changed(prev_mat, mat):
    if np.array_equal(prev_mat, mat):
        return False
    else:
        return True

mat = map2mat(puzzle_input)
finished = False
cnt=0
while not finished:  
    cnt+=1    
    print(cnt)  
    mat_new = evolve(mat)
    if not has_changed(mat_new, mat):
        finished = True
        print(f'part 1 result = {np.sum(mat_new==2)}')
    else:
        mat = mat_new.copy()


# part 2
def is_out_of_bounds(mat, i, j):
    if i<0 or j<0 or i>mat.shape[0]-1 or j>mat.shape[1]-1:
        return True
    else:
        return False
    

def occupied_in_view(mat,i,j):
    # [row,col]
    directions = [[-1,-1], [-1,0], [-1,1], [1,1], [1,-1], [1,0], [0,1], [0,-1]]
    sum_occupied = 0
    for d in directions:
        cur_i = i
        cur_j = j
        while True:
            next_i = cur_i + d[0]
            next_j = cur_j + d[1]
            cur_i = next_i
            cur_j = next_j
            if is_out_of_bounds(mat, next_i, next_j):
                break
            if mat[next_i, next_j] == 1:
                break
            elif mat[next_i, next_j] == 2:
                sum_occupied += 1
                break
    return sum_occupied


def evolve2(mat):
    mat_new = mat.copy()
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            if mat[i,j] == 1 and occupied_in_view(mat, i, j) == 0:
                mat_new[i,j] = 2
            if mat[i,j] == 2 and occupied_in_view(mat, i, j)>=5:
                mat_new[i,j] = 1

    return mat_new

mat = map2mat(puzzle_input)
finished = False
cnt=0
while not finished:  
    cnt+=1    
    print(cnt)  
    mat_new = evolve2(mat)
    if not has_changed(mat_new, mat):
        finished = True
        print(f'part 2 result = {np.sum(mat_new==2)}')
    else:
        mat = mat_new.copy()