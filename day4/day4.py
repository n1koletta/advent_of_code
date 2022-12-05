
#part 1

count = 0
with open('input_day4.txt','r') as f:
    for line in f:
        pairs = line.strip().split(',')
        pair1 = pairs[0].split('-')
        pair2 =  pairs[1].split('-')
        if (int(pair2[0])>=int(pair1[0]) and int(pair2[1])<= int(pair1[1])) or (int(pair1[0])>=int(pair2[0]) and int(pair1[1])<=int(pair2[1])):
            print (pair1, pair2)
            count+=1
        
print(count)

#part2
count = 0
with open('input_day4.txt','r') as f:
    for line in f:
        pairs = line.strip().split(',')
        pair1 = pairs[0].split('-')
        pair2 =  pairs[1].split('-')
        pair1 = [*range(int(pair1[0]),int(pair1[1])+1)]
        pair2 = [*range(int(pair2[0]),int(pair2[1])+1)]
        if any(x in pair1 for x in pair2):
            count+=1

print(count)