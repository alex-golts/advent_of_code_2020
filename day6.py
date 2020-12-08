f = open('input6.txt','r')
txt = f.read()
puzzle_input = [item.split('\n') for item in txt.split('\n\n')]

joined_input = [''.join(item) for item in puzzle_input]
cnt_unique = [len(set(item)) for item in joined_input] 

print(f'part 1 answer = {sum(cnt_unique)}')

# part 2:
set_input = [[set(a) for a in item] for item in puzzle_input]
cnt_common = [len(set.intersection(*item)) for item in set_input]

print(f'part 2 answer = {sum(cnt_common)}')
