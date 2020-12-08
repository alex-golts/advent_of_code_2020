f = open('input1.txt','r')
txt = f.read()
txt = txt.split('\n')
puzzle_input = [int(a) for a in txt]

import numpy as np

# part 1:
sum_mat = np.zeros((len(puzzle_input), len(puzzle_input)))
for i in range(sum_mat.shape[0]):
    for j in range(sum_mat.shape[1]):
        if i==j:
            continue
        sum_mat[i,j] = puzzle_input[i]+puzzle_input[j]
        if sum_mat[i,j]==2020:
            print(f'part 1 result = {puzzle_input[i]*puzzle_input[j]}')


# part 2:
sum_mat = np.zeros((len(puzzle_input), len(puzzle_input), len(puzzle_input)))
for i in range(sum_mat.shape[0]):
    for j in range(sum_mat.shape[1]):
        for k in range(sum_mat.shape[2]):
            if i==j or i==k or j==k:
                continue
            sum_mat[i,j,k] = puzzle_input[i]+puzzle_input[j]+puzzle_input[k]
            if sum_mat[i,j,k]==2020:
                print(f'part 2 result = {puzzle_input[i]*puzzle_input[j]*puzzle_input[k]}')
