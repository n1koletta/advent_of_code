def read_input(filename):
    with open(filename, 'r') as f:
        input = f.read().splitlines()

    return input

input = read_input('day9_input.txt')

class Point:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def move(self,direction):
        if direction == 'U':
            self.move_up()
        elif direction == 'D':
            self.move_down()
        elif direction == 'L':
            self.move_left()
        elif direction == 'R':
            self.move_right()
        else:
            raise ValueError


    def move_up(self):
        self.y += 1

    def move_down(self):
        self.y -= 1
    
    def move_left(self):
        self.x -= 1

    def move_right(self):
        self.x += 1 
    
head = Point(0,0)
tail = Point(0,0)

unique_locations = {(tail.x,tail.y)}

for line in input:
    direction = line.split()[0]
    steps = int(line.split()[1])
    print(line)
    for _ in range(steps):
        print(_)
        head.move(direction)

        if abs(tail.x - head.x) > 1 or abs(tail.y - head.y) > 1:
            tail.x += (0 if tail.x == head.x else (head.x - tail.x)//abs(tail.x - head.x)) #the else gives just signed 1
            tail.y += (0 if tail.y == head.y else (head.y - tail.y)//abs(tail.y - head.y))

        unique_locations.add((tail.x,tail.y))

        print(head.x,head.y)
        print(tail.x,tail.y)

print(len(unique_locations))

