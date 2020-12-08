f = open('input4.txt','r')
txt = f.read()
txt = txt.split('\n')

passport_list = []

passport_list.append({})
ind = 0
for l in txt:
    if l=='':
        ind+=1
        passport_list.append({})
        continue
    key_vals = l.split(' ')
    for k in key_vals:
        pair = k.split(':')
        passport_list[ind][pair[0]] = pair[1]
        
required_fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
def is_valid(passport, required_fields):
    for f in required_fields:
        if f not in passport:
            return False
    return True

cnt_invalid = sum([int(not is_valid(p, required_fields)) for p in passport_list])

print(f'part 1 answer = {len(passport_list) - cnt_invalid}')

# part 2:
def is_valid2(passport, required_fields):
    for f in required_fields:
        if f not in passport:
            return False
        if f == 'byr' and (not passport[f].isnumeric() or int(passport[f])<1920 or int(passport[f])>2002):
            return False
        if f == 'iyr' and (not passport[f].isnumeric() or int(passport[f])<2010 or int(passport[f])>2020):
            return False
        if f == 'eyr' and (not passport[f].isnumeric() or int(passport[f])<2020 or int(passport[f])>2030):
            return False
        if f == 'hgt' and (not passport[f].endswith('cm') and not passport[f].endswith('in')):
            return False
        if f == 'hgt' and passport[f].endswith('cm') and (int(passport[f][:-2])<150 or int(passport[f][:-2])>193):
            return False
        if f == 'hgt' and passport[f].endswith('in') and (int(passport[f][:-2])<59 or int(passport[f][:-2])>76):
            return False
        if f == 'hcl' and (not passport[f].startswith('#') or len(passport[f])!=7):
            return False
        if f == 'hcl':
            for c in passport[f][1:]:
                if not c.isnumeric() and (c>'f' or c<'a'):
                    return False
        if f == 'ecl' and passport[f] not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
            return False
        if f == 'pid' and (not passport[f].isnumeric() or len(passport[f])!=9):
            return False
         
    return True

cnt_invalid = sum([int(not is_valid2(p, required_fields)) for p in passport_list])

print(f'part 2 answer = {len(passport_list) - cnt_invalid}')