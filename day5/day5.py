'''
                    [L]     [H] [W]
                [J] [Z] [J] [Q] [Q]
[S]             [M] [C] [T] [F] [B]
[P]     [H]     [B] [D] [G] [B] [P]
[W]     [L] [D] [D] [J] [W] [T] [C]
[N] [T] [R] [T] [T] [T] [M] [M] [G]
[J] [S] [Q] [S] [Z] [W] [P] [G] [D]
[Z] [G] [V] [V] [Q] [M] [L] [N] [R]
 1   2   3   4   5   6   7   8   9 

s1 = ['Z','J','N','W','P','S']
s2 = ['G','S','T']
s3 = ['V','Q','R','L','H']
s4 = ['V','S','T','D']
s5 = ['Q','Z','T','D','B','M','J']
s6 = ['M','W','T','J','D','C','Z','L']
s7 = ['L','P','M','W','G','T','J']
s8 = ['N','G','M','T','B','F','Q','H']
s9 = ['R','D','G','C','P','B','Q','W']

'''


# PART 1 
stacks = [ ['Z','J','N','W','P','S'], ['G','S','T'], ['V','Q','R','L','H'], ['V','S','T','D'], ['Q','Z','T','D','B','M','J'], ['M','W','T','J','D','C','Z','L'], ['L','P','M','W','G','T','J'], ['N','G','M','T','B','F','Q','H'], ['R','D','G','C','P','B','Q','W'] ]

def pick_crates(number_of_crates,start_stack):
    selected_crates = start_stack[-1:(-number_of_crates-1):-1]
    return selected_crates

def remove_crates(start_stack,number_of_crates):
    del start_stack[-1:(-number_of_crates-1):-1]


def place_crates(list_of_crates,end_stack):
    for crate in (list_of_crates):
        end_stack.append(crate)
    return end_stack


with open('input_day5.txt', 'r') as f:
    
    for line in f:
        action = line.strip().split(' ')
        number_of_crates = int(action[1])
        start_stack = int(action[3]) -1 
        destination_stack = int(action[5])-1

        crates_selected = pick_crates(number_of_crates,stacks[start_stack][:])
        remove_crates(stacks[start_stack],number_of_crates)

        end_stack = place_crates(crates_selected,stacks[destination_stack][:])
        stacks[destination_stack][:] = end_stack[:]
        

#answer
answer = "".join([x[-1] for x in stacks])
print(answer)



# PART 2 

stacks = [ ['Z','J','N','W','P','S'], ['G','S','T'], ['V','Q','R','L','H'], ['V','S','T','D'], ['Q','Z','T','D','B','M','J'], ['M','W','T','J','D','C','Z','L'], ['L','P','M','W','G','T','J'], ['N','G','M','T','B','F','Q','H'], ['R','D','G','C','P','B','Q','W'] ]

def pick_crates(number_of_crates,start_stack):
    selected_crates = start_stack[-number_of_crates:]
    return selected_crates

def remove_crates(start_stack,number_of_crates):
    del start_stack[-number_of_crates:]


def place_crates(list_of_crates,end_stack):
    for crate in (list_of_crates):
        end_stack.append(crate)
    return end_stack


with open('input_day5.txt', 'r') as f:
    
    for line in f:
        action = line.strip().split(' ')
        number_of_crates = int(action[1])
        start_stack = int(action[3]) -1 
        destination_stack = int(action[5])-1

        crates_selected = pick_crates(number_of_crates,stacks[start_stack][:])
        remove_crates(stacks[start_stack],number_of_crates)

        end_stack = place_crates(crates_selected,stacks[destination_stack][:])
        stacks[destination_stack][:] = end_stack[:]
        print(stacks)

#answer
answer = "".join([x[-1] for x in stacks])
print(answer)