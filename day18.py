import re

f = open('input18.txt','r')
txt = f.read()
txt = txt.split('\n')
puzzle_input = txt[:-1]

def remove_brackets(expression):
    # remove first brackets from expression that starts with '('
    cnt_paren = 0
    for i,c in enumerate(expression):
        if c == '(':
            cnt_paren+=1
        if c == ')':
            cnt_paren-=1
        if cnt_paren == 0:
            last_i = i
            break
    return expression[1:last_i]+expression[last_i+1:], last_i

def solve(expression):
    if expression.isnumeric():
        return expression
    
    if expression[0] == '(':
        expression, _ = remove_brackets(expression)
        return solve(expression)
        
    else:
        # find first op:
        for i,c in enumerate(expression):
            if c in ('*','+'):
                first_op = c
                first_op_ind = i
                break
        left_side = expression[0:first_op_ind]
        
        if left_side.isnumeric() and not expression[first_op_ind+1].isdigit():
            _,last_bracket_ind = remove_brackets(expression[first_op_ind+1:])
            if first_op == '*':
                expression = str(int(left_side) * int(solve(expression[first_op_ind+2:first_op_ind+last_bracket_ind+1]))) + expression[first_op_ind + last_bracket_ind+2:]
            elif first_op == '+':
                expression = str(int(left_side) + int(solve(expression[first_op_ind+2:first_op_ind+last_bracket_ind+1]))) + expression[first_op_ind + last_bracket_ind+2:]
            return solve(expression)

        if left_side.isnumeric() and expression[first_op_ind+1].isdigit():
            if first_op == '*':
                expression = str(int(left_side) * int(expression[first_op_ind+1])) + expression[first_op_ind+2:]
            elif first_op == '+':
                expression = str(int(left_side) + int(expression[first_op_ind+1])) + expression[first_op_ind+2:]
            return solve(expression)
    
results = []
for line in puzzle_input:
    line2 = line.replace(' ','')
    results.append(int(solve(line2)))

print(f'part 1 answer = {sum(results)}')

################################################################################
# part 2:

def get_trailing_number(s):
    m = re.search(r'\d+$', s)
    return m.group() if m else None

def get_starting_number(s):
    m = re.match(r'\d+', s)
    return m.group() if m else None

def solve2(expression):
    if expression.isnumeric():
        return expression
    # look for parentheses
    paren_ind = expression.find('(')
    if paren_ind>-1:
        # find closing parentheses
        expression_without_parens, last_ind = remove_brackets(expression[paren_ind:]) 
        closing_paren_ind = paren_ind + last_ind
        # if expression is of the form ($something), then just return the solution for $something
        if paren_ind == 0 and closing_paren_ind == len(expression)-1:
            return solve2(expression_without_parens)
        expression = expression[0:paren_ind]+solve2(expression[paren_ind:closing_paren_ind+1])+expression[closing_paren_ind+1:]
        return solve2(expression)
    plus_ind = expression.find('+')
    if plus_ind>-1:
        left_side = expression[0:plus_ind]
        right_side = expression[plus_ind+1:]
        left_final_num = get_trailing_number(left_side)
        right_first_num = get_starting_number(right_side)
        if left_final_num is not None and right_first_num is not None:
            left_side = left_side[0:-len(left_final_num)]
            right_side = right_side[len(right_first_num):]
            expression =  left_side + str(int(left_final_num)+int(right_first_num)) + right_side
            return solve2(expression)
        if left_final_num is not None and right_first_num is None:
            left_side = left_side[0:-len(left_final_num)]
            expression = left_side + str(int(left_final_num)+int(solve2(right_side)))
            return solve2(expression)
        if left_final_num is None and right_first_num is not None:
            right_side = right_side[len(right_first_num):]
            expression = str(int(solve2(left_side))+int(right_first_num)) + right_side
            return solve2(expression)
        if left_side.isnumeric() and right_side.isnumeric():
            return str(int(left_side)+int(right_side)) 
        else:
            return str(int(solve2(left_side))+int(solve2(right_side)))
    else:
        return str(eval(expression))

results = []
for line in puzzle_input:
    line2 = line.replace(' ','')
    results.append(int(solve2(line2)))

print(f'part 2 answer = {sum(results)}')

