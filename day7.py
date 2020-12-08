import re
# parse input:
f = open('input7.txt','r')
txt = f.read()
txt = txt.split('\n')
puzzle_input = txt

class Bag(object):
    def __init__(self, color, parents=None):
        self.color = color
        self.contents = []
        self.contents_count = []
        self.parents = []

    def add_content(self, bag, count):
        self.contents.append(bag)
        self.contents_count.append(count)

    def is_child_of(self, bag):
        # is self a child of bag
        if len(self.parents)==0:
            return False
        for p in self.parents:
            if p.color == bag.color:
                return True
        return False
    
    def print_parents(self):
        for p in self.parents:
            print(p.color)
    
    def print_contents(self):
        for c in self.contents:
            print(c.color)


# create a dictionary of unique color bags - this is our tree    
tree = {}

# parse input and create the tree:
# really ugly parsing, sorry :(
for line in puzzle_input:
    # find occurances of word 'bag' 
    matches = re.finditer('bag', line)
    bag_str_positions = [match.start() for match in matches]
    
    subject_color = line[0:bag_str_positions[0]-1]

    if subject_color not in tree:
        tree[subject_color] = Bag(subject_color)

    # find occurances of word 'contain'
    contain_str_position = line.find('contain')
    # find occurances of comma
    matches = re.finditer(',', line)
    comma_positions = [match.start() for match in matches]

    matches = re.finditer(' ', line[contain_str_position:bag_str_positions[1]-1])
    space_after_1st_num_position = [match.start() for match in matches][1]+contain_str_position
    content_1_color = line[space_after_1st_num_position+1:bag_str_positions[1]-1]
    if line[contain_str_position+8:space_after_1st_num_position] == 'no':
        continue
    content_1_count = int(line[contain_str_position+8:space_after_1st_num_position])
    
    if content_1_color not in tree:
        tree[content_1_color] = Bag(content_1_color)
    if not tree[content_1_color].is_child_of(tree[subject_color]):
        tree[content_1_color].parents.append(tree[subject_color])
        tree[subject_color].add_content(tree[content_1_color], content_1_count)

    for ind,pos in enumerate(comma_positions):
        matches = re.finditer(' ', line[comma_positions[ind]:])
        space_after_num_position = [match.start() for match in matches][1]+comma_positions[ind]
        content_color = line[space_after_num_position+1:bag_str_positions[ind+2]-1]
        content_count = int(line[comma_positions[ind]+2:space_after_num_position])

        if content_color not in tree:
            tree[content_color] = Bag(content_color)
        if not tree[content_color].is_child_of(tree[subject_color]):
            tree[content_color].parents.append(tree[subject_color])
            tree[subject_color].add_content(tree[content_color], content_count)


# the answer in part A is the number of possible anscestors of the bag 'shiny gold'

def get_unique_anscestors(bag):
    # return a set containing unique anscestors
    if len(bag.parents) == 0:
        return set()
    else:
        parents = set(bag.parents)
        for p in bag.parents:
            parents = parents | get_unique_anscestors(p)
    return parents


shiny_gold_bag = tree['shiny gold']
print(f'part 1 answer = {len(get_unique_anscestors(shiny_gold_bag))}')

# part 2:

# the answer is the number of descendants (their respective count) of 'shiny gold' bag

def num_descendants(bag):
    # return a set containing unique anscestors
    if len(bag.contents) == 0:
        return 0
    else:
        contents = bag.contents
        contents_count = bag.contents_count
        cnt = 0
        for i,c in enumerate(contents):
            cnt += contents_count[i] + contents_count[i]*num_descendants(c)
    return cnt

print(f'part 2 answer = {num_descendants(shiny_gold_bag)}')
