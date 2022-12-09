from tree import Tree

with open('input_day7.txt','r') as f:
    output = f.read().splitlines()


t = Tree()

for line in output:
    if line[0] == '$': #it's a cmd
        folder = line.split()[-1]
        if folder == '..': #go to previous dir
            t.go_up()
        else:
            t.add_node(folder)
    else:
        size,name = line.split()
        if size !='dir':
            t.add_node(name,int(size))

t.update_sizes()

print(sum(filter(lambda x: x <= 100000, t.dirs)))