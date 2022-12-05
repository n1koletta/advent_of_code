def check_score(opponent, elf):
    if opponent == 'A':
        if elf == 'X':
            return 3
        elif elf == 'Y':
            return 4
        else:
            return 8

    elif opponent == 'B':
        if elf == 'X':
            return 1
        elif elf == 'Y':
            return 5
        else:
            return 9

    else:
        if elf == 'X':
            return 2
        if elf == 'Y':
            return 6 
        else:
            return 7

score = 0
with open ('input_day2.txt', 'r') as file:
    for line in file:
        opponent, elf = line[0], line[2]
        score += check_score(opponent,elf)

print(score)