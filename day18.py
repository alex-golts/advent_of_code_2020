f = open('input18.txt','r')
txt = f.read()
txt = txt.split('\n')
puzzle_input = txt[:-1]


#sample = '2 * 3 + (4 * 5)'
#sample = '2 * 3 + 1'
#sample = '5 + (8 * 3 + 9 + 3 * 4 * 3)'
#sample = '5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'
sample = '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'
sample = sample.replace(' ','')



def solve(expression):
    if expression.isnumeric():
        return expression
    
    if expression[0] == '(':
        cnt_paren = 0
        for i,c in enumerate(expression):
            if c == '(':
                cnt_paren+=1
            if c == ')':
                cnt_paren-=1
            if cnt_paren == 0:
                last_i = i
                break
        #paren_str = expression[0:last_i]
        
        return solve(expression[1:last_i]+expression[last_i+1:])
    
    else:
        # find first op:
        for i,c in enumerate(expression):
            if c in ('*','+'):
                first_op = c
                first_op_ind = i
                break
        left_side = expression[0:first_op_ind]
        
        
        if left_side.isnumeric() and not expression[first_op_ind+1].isdigit():
            if first_op == '*':
                return str(int(left_side) * int(solve(expression[first_op_ind+1:])))
            elif first_op == '+':
                return str(int(left_side) + int(solve(expression[first_op_ind+1:])))
        
        if left_side.isnumeric() and expression[first_op_ind+1].isdigit():
            if first_op == '*':
                expression = str(int(left_side) * int(expression[first_op_ind+1])) + expression[first_op_ind+2:]
            elif first_op == '+':
                expression = str(int(left_side) + int(expression[first_op_ind+1])) + expression[first_op_ind+2:]
            return solve(expression)
    
    
        

print(solve(sample))
