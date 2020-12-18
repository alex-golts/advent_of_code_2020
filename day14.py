f = open('input14.txt','r')
txt = f.read()
puzzle_input = txt.split('\n')[:-1]

def parse_line(line):
    eq_sign_ind = line.find('=')
    if line.startswith('mask'):
        binary_str = line[eq_sign_ind+2:]
        return 'mask', binary_str, None
    if line.startswith('mem'):
        open_bracket_ind = line.find('[')
        close_bracket_ind = line.find(']')
        mem = int(str(line[open_bracket_ind+1:close_bracket_ind]))
        val = int(str(line[eq_sign_ind+2:]))
        return 'mem', mem, val
        
memory = {}
for line in puzzle_input:
    typ, arg1, arg2 = parse_line(line)
    if typ=='mask':
        cur_mask = arg1
    if typ=='mem':
        val_bin_str = bin(arg2)[2:].zfill(36)
        actual_bin_str = [c for c in val_bin_str]
        # apply mask:
        for i,c in enumerate(cur_mask):
            if c == '0':
                actual_bin_str[i] = '0'
            if c == '1':
                actual_bin_str[i] = '1'
        actual_int = int(''.join(actual_bin_str), 2)
        memory[arg1] = actual_int
    
tot_sum = 0
for key in memory:
    tot_sum += memory[key]

print(f'part 1 answer = {tot_sum}')
                