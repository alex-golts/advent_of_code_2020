f = open('input8.txt','r')
txt = f.read()
txt = txt.split('\n')
puzzle_input = txt


def execute_instruction(instruction, accumulator, pos, already_executed):
    already_executed[pos] += 1
    argument = int(instruction[4:])
    inst = instruction[0:3]
    if inst == 'nop':
        pos += 1
    elif inst == 'jmp':
        pos += argument
    elif inst == 'acc':
        accumulator += argument
        pos += 1
    return accumulator, pos, already_executed

def execute_all(instruction_list):
    accumulator = 0
    pos = 0
    already_executed = [0 for i in range(len(instruction_list))]
    finished = 0
    while True:
        prev_accumulator = accumulator
        prev_pos = pos
        accumulator, pos, already_executed = \
            execute_instruction(instruction_list[pos], accumulator, pos, already_executed)
        if already_executed[prev_pos]==2:
            return finished, prev_accumulator, accumulator
        if pos == len(instruction_list):
            finished = 1
            return finished, prev_accumulator, accumulator

_, prev_accumulator, _ = execute_all(puzzle_input)
print(f'part 1 result = {prev_accumulator}')

# part 2:
for ind,inst in enumerate(puzzle_input):
    cur_list = puzzle_input.copy()
    if inst[0:3] == 'jmp':
        cur_list[ind] = cur_list[ind].replace('jmp','nop')
    elif inst[0:3] == 'nop':
        cur_list[ind] = cur_list[ind].replace('nop','jmp')
    else:
        continue
    finished,_,cur_accumulator = execute_all(cur_list)
    if finished == 1:
        print(f'part 2 result = {cur_accumulator}')
        break
        

