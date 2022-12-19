#function to read input
def read_input(filename):
    with open(filename,'r') as f:
        input = f.read().splitlines()
    return input

input = read_input('day10_input.txt')

def check_cycle(cycle):
    if cycle == 20 or (cycle+20)%40 ==0:
        return x*cycle
    else: return 0

x=1
cycle = 0
signal_strength = 0

for line in input:

    l = line.split()

    if l[0] == 'noop':
        cycle +=1
        signal_strength += check_cycle(cycle)

    else:
        cycle +=1
        signal_strength += check_cycle(cycle)

        cycle+=1
        signal_strength += check_cycle(cycle)
        x += int(l[1])

        

print('Signal Strength: ',signal_strength)


