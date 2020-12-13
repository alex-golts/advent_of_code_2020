import numpy as np

f = open('input10.txt','r')
txt = f.read()
txt = txt.split('\n')[:-1]
puzzle_input = [int(item) for item in txt]

vec = sorted(puzzle_input)
vec.insert(0,0)
vec.append(max(vec)+3)
vec = np.array(vec)
diff_vec = np.diff(vec)

diff1 = (diff_vec==1).sum()
diff3 = (diff_vec==3).sum()
print(f'part 1 result = {diff1*diff3}')

# part 2:

# observe there are only diffs of 1 and 3. diff 3 locations cannot move
# there are length 1, 2, 3 and 4 sequences of diff 1
# lenght 1 sequence cannot be rearranged
# length 2 sequence has 2 ways to be rearranged (remove 1st or 2nd element)
# length 3 sequence has 4 ways to be rearranged (manually enumerated)
# length 4 sequence has 7 ways to be rearranged (manually enumerated)

# find sequence 1 lengths:
seq1_lengths = []
cnt = 0
for i in range(len(diff_vec)):
    if diff_vec[i] == 1:
        cnt+=1
    if diff_vec[i] == 3:
        if cnt!=0:
            seq1_lengths.append(cnt)
        cnt=0

seq_rearrangements = []
for item in seq1_lengths:
    if item==1:
        seq_rearrangements.append(1)
    elif item==2:
        seq_rearrangements.append(2)
    elif item==3:
        seq_rearrangements.append(4)
    elif item==4:
        seq_rearrangements.append(7)


def product(list):
    p = 1
    for i in list:
        p *= i
    return p

print(f'part 2 results = {product(seq_rearrangements)}')
