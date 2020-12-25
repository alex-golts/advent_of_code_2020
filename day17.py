import numpy as np

f = open('input17.txt','r')
txt = f.read()
txt = txt.split('\n')
puzzle_input = txt[:-1]

def lst2mat(lst):
    mat = np.zeros((len(lst), len(lst[0])))
    for i in range(len(lst)):
        for j in range(len(lst[0])):
            if lst[i][j] == '#':
                mat[i,j] = 1
    return mat

mat = lst2mat(puzzle_input)
# add zeros in z dimension:
zeros_mat = np.zeros((mat.shape[0], mat.shape[1]))
mat = np.stack((zeros_mat, mat, zeros_mat), axis=2)

def num_active_neighbors(mat, i, j, k):
    cnt = 0
    for di in range(-1,2):
        for dj in range(-1,2):
            for dk in range(-1,2):
                if di==dj==dk==0:
                    continue
                
                if (i+di)<0 or (i+di)>=mat.shape[0]:
                    continue
                if (j+dj)<0 or (j+dj)>=mat.shape[1]:
                    continue
                if (k+dk)<0 or (k+dk)>=mat.shape[2]:
                    continue
                if mat[i+di, j+dj, k+dk]==1:
                    cnt+=1
    return cnt

def cycle(mat):
    mat = np.pad(mat, 1, mode='constant', constant_values=0)
    new_mat = np.zeros_like(mat)
    for i in range(new_mat.shape[0]):
        for j in range(new_mat.shape[1]):
            for k in range(new_mat.shape[2]):
                num_active = num_active_neighbors(mat, i, j, k)
                if mat[i,j,k]==1:
                    if (num_active==2 or num_active==3):
                        new_mat[i,j,k] = 1
                    else:
                        new_mat[i,j,k] = 0
                if mat[i,j,k]==0: 
                    if num_active==3:
                        new_mat[i,j,k] = 1
                    else:
                        new_mat[i,j,k] = 0
                    
    return new_mat

new_mat = mat.copy()
for i in range(1,6+1):
    new_mat = cycle(new_mat)
    
print(f'part 1 answer = {int(np.sum(new_mat))}')
    

# part 2

def num_active_neighbors_4d(mat, i, j, k, l):
    cnt = 0
    for di in range(-1,2):
        for dj in range(-1,2):
            for dk in range(-1,2):
                for dl in range(-1,2):
                    if di==dj==dk==dl==0:
                        continue
                    
                    if (i+di)<0 or (i+di)>=mat.shape[0]:
                        continue
                    if (j+dj)<0 or (j+dj)>=mat.shape[1]:
                        continue
                    if (k+dk)<0 or (k+dk)>=mat.shape[2]:
                        continue
                    if (l+dl)<0 or (l+dl)>=mat.shape[3]:
                        continue
                    if mat[i+di, j+dj, k+dk, l+dl]==1:
                        cnt+=1
    return cnt

def cycle_4d(mat):
    mat = np.pad(mat, 1, mode='constant', constant_values=0)
    new_mat = np.zeros_like(mat)
    for i in range(new_mat.shape[0]):
        for j in range(new_mat.shape[1]):
            for k in range(new_mat.shape[2]):
                for l in range(new_mat.shape[3]):
                    num_active = num_active_neighbors_4d(mat, i, j, k, l)
                    if mat[i,j,k,l]==1:
                        if (num_active==2 or num_active==3):
                            new_mat[i,j,k,l] = 1
                        else:
                            new_mat[i,j,k,l] = 0
                    if mat[i,j,k,l]==0: 
                        if num_active==3:
                            new_mat[i,j,k,l] = 1
                        else:
                            new_mat[i,j,k,l] = 0
                    
    return new_mat

mat = lst2mat(puzzle_input)
# add zeros in z dimension:
zeros_mat = np.zeros((mat.shape[0], mat.shape[1]))
mat = np.stack((mat, zeros_mat, zeros_mat), axis=2)
zeros_cube = np.zeros((mat.shape[0], mat.shape[1], 3))
mat = np.stack((mat, zeros_cube, zeros_cube), axis=3)


new_mat = mat.copy()
for i in range(1,6+1):
    new_mat = cycle_4d(new_mat)
    
print(f'part 2 answer = {int(np.sum(new_mat))}')
