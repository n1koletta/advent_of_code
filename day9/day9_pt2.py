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

    def __str__(self):
        return 'Point: {} {}'.format(self.x, self.y)

    def __repr__(self):
        return str((self.x,self.y))

    def move_up(self):
        self.y += 1

    def move_down(self):
        self.y -= 1
    
    def move_left(self):
        self.x -= 1

    def move_right(self):
        self.x += 1 


#create the knots  
points = [Point(0,0) for _ in range(10)]


for line in input:
    direction = line.split()[0]
    steps = int(line.split()[1])
    print(line)

    for index,_ in enumerate(range(steps)):
        print(index)
        for i in range(index+1):
            points[index-i].move(direction) #move the head by one

        '''if abs(tail.x - head.x) > 9 or abs(tail.y - head.y) > 9:
            tail.x += (0 if tail.x == head.x else (head.x - tail.x)//abs(tail.x - head.x)) #the else gives just signed 1
            tail.y += (0 if tail.y == head.y else (head.y - tail.y)//abs(tail.y - head.y))
'''




