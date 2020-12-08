f = open('input2.txt','r')
txt = f.read()
txt = txt.split('\n')
puzzle_input = txt

def find_pattern(s):
    hyphen_ind = s.find('-')
    first_num = int(s[0:hyphen_ind])
    space_ind = s.find(' ')
    colon_ind = s.find(':')
    ch = s[space_ind+1:space_ind+2]
    second_num = int(s[hyphen_ind+1:space_ind])
    passwd = s[colon_ind+2:]

    return (first_num, second_num, ch, passwd)

def is_valid(s, pat):
    cnt = s.count(pat[2])
    if cnt >= pat[0] and cnt <= pat[1]:
        return True
    else:
        return False

def is_valid2(s, pat):
    cnt=0
    if s[pat[0]-1]==pat[2]:
        cnt+=1
    if s[pat[1]-1]==pat[2]:
        cnt+=1
    if cnt==1:
        return True
    else:
        return False

cnt=0
for s in puzzle_input:
    pat = find_pattern(s)
    cnt+=int(is_valid(pat[-1], pat))

print(f'part 1 results={cnt}')

# part 2:

cnt=0
for s in puzzle_input:
    pat = find_pattern(s)
    cnt+=int(is_valid2(pat[-1], pat))

print(f'part 2 results={cnt}')