import numpy as np

f = open('input9.txt','r')
txt = f.read()
txt = txt.split('\n')
puzzle_input = [int(item) for item in txt]

def sumMat(numList):
    rowArr = np.tile(np.array(numList)[np.newaxis, :], (len(numList), 1))
    colArr = np.tile(np.array(numList)[:, np.newaxis], (1, len(numList)))
    sumArr = rowArr + colArr
    # put some large number on the diagonal that won't effect result
    np.fill_diagonal(sumArr, 1e16)
    return sumArr

def is_valid(curNum, sumArr, ind):
    return np.any(sumArr[ind-25:ind, ind-25:ind]==curNum)    

sumArr = sumMat(puzzle_input)
for ind,curNum in enumerate(puzzle_input):
    if ind>=25:
        #inds = np.linspace(ind-25,ind-1,25).astype('int')
        if not is_valid(curNum, sumArr, ind):
            res = curNum
            print(f'part 1 result = {res}')
            break

# part 2

# create a matrix where each element i,j is the sum of element i until j
def cumSumMat(numList):
    numArr = np.array(numList)
    cumSumArr = np.zeros((len(numList), len(numList)))
    for i in range(len(numList)):
        for j in range(len(numList)):
            cumSumArr[i,j] = np.sum(numArr[i:j])
    return cumSumArr

cumSumArr = cumSumMat(puzzle_input)
solved_part_2 = False
for ind,curNum in enumerate(puzzle_input):
    for i in range(ind):
        if cumSumArr[i,ind]==res:
            minVal = min(puzzle_input[i:ind])
            maxVal = max(puzzle_input[i:ind])
            print(f'part 2 result = {minVal+maxVal}')
            solved_part_2 = True
            break
    if solved_part_2:
        break

