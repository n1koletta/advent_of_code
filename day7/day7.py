#1. combine directories and content into dictionary
def dictionarise_directory_structure():
    directory = {} 
    with open('input_day7.txt','r') as f:
        temp = []
        for line in f:
            if line.strip().split(' ')[1] == 'cd' :
                temp = []
                dict_name = line.strip().split(' ')[2]
                continue
            elif line.strip().split(' ')[1] != 'ls':
                temp.append(line.strip())
            else:
                continue
            directory[dict_name]=temp
    return directory

#2. seperate files and folders within each directory

def struct_directory(directory_structure):
    for dir_name, contents in directory_structure.items():      
        for i,val in enumerate(contents):
            keyword_of_val = val.split(' ')[0]
            if keyword_of_val.isnumeric(): #check if the first part of the name is numeric - means it's a file
                directory_structure[dir_name][i]=int(keyword_of_val)
            elif keyword_of_val == 'dir': #check if the first part of the name is 'dir' - means it's a nested directory
                directory_structure[dir_name][i]=val.split(' ')[1]
            else:
                continue
    structured_directory = directory_structure
    return structured_directory

#3. calculate if any directories contain just files and if so to calculate their size 
def sumup_directory(directory):
    for dir_name, contents in directory.items(): 
        if all([isinstance(val, int) for val in contents]): #if all elements are numeric inside a directory  (i.e. you reached the end of that branch), find their sum
            directory[dir_name]=sum(contents)
    return directory

#4. create a dictionary that contains only the known sizes that have been calculated for each directory 
def known_size_directories(directory):
    known_size = {}
    for key,val in directory.items():
        if isinstance(val,int):
            known_size[key] = val
    return known_size

#5. create a dictionary that contains only the unknown size directories 
def unknown_size(dir, known_size_directories):
     return {x: dir[x] for x in dir if x not in known_size_directories.keys()}


#6. substitute the sizes of various directories based on the dictionary with the known sizes

def map_from_known_to_unknown(known_dir,unknown_dir):
    for key,value in unknown_dir.items():
        for i,val in enumerate(value):
            if val in known_dir.keys():
                unknown_dir[key][i] = known_dir[val]
    return unknown_dir

#7. repeat stesp 4-6 until all directory sizes calculated

#1
directories_dict = dictionarise_directory_structure()

#2
dir= struct_directory(directories_dict)

#3
dir = sumup_directory(dir)

#4.
known = known_size_directories(dir)

#5
unknown = unknown_size(dir,known)

def print_dict(dict):
    for k,v in dict.items():
        print(k,':',v)
        print()

output = known
while unknown:
    
    dir = map_from_known_to_unknown(known,unknown)
    dir = sumup_directory(dir)
    known = known_size_directories(dir)
    unknown = unknown_size(dir,known)
    output.update(known) #stores the latest values for each dir to access them after the while loop ends


#Part 1: Find the sum of all directories with size<100K

sum = 0
for k,v in output.items():
    if v<=100_000:
        sum+=v

print(sum)
