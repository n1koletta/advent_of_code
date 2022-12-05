import string

priorityMapLower = dict(zip(string.ascii_lowercase, [x for x in range(1, 27)]))
priorityMapUpper = dict(zip(string.ascii_uppercase, [x for x in range(27, 53)]))
priorityMap = {**priorityMapLower, **priorityMapUpper}

'''priority = 0
with open('input_day3.txt', 'r') as f:
    for line in f:
        midpoint = len(line)//2
        c1 = line[:midpoint]
        c2 = line[midpoint:]
        common_letter = set(c1).intersection(c2)
        priority += priorityMap[common_letter.pop()]
        
print(priority)'''


#create list of lists. Each list inside the main list contains three runsacks. 
#identify the common letter within each list
#then calculate priorty

#common letter
def common_letter_in(l):
    return (set(l[0]) & set(l[1]) & set(l[2])).pop()

with open('input_day3.txt','r') as f:
    groups_main = []
    lst = []
    for number,line in enumerate(f):
        if number%3 !=0 or number ==0:
            lst.append(line.strip())
        else:
            groups_main.append(lst)
            lst = []
            lst.append(line.strip())
        
            

        
        

priority = 0        
for l in groups_main:
    #priority += priorityMap[common_letter_in(l)]
    print(l)