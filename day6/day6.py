#read-in input

with open( 'input_day6.txt', 'r') as f:
    signal = f.readlines()
signal = signal[0]


#part1
for index,char in enumerate(signal):
    character_packet = signal[index:index+4]
    if len(set(character_packet))==4:
        print('Part 1 Answer: ',index+4)
        break

#part2
for index,char in enumerate(signal):
    character_packet = signal[index:index+14]
    if len(set(character_packet))==14:
        print('Part 2 Answer: ',index+14)
        break