with open('day11_input.txt', 'r') as f:
    #input = [p.strip() for p in f.read().split('\n\n')]
    input = f.read()
    

input_iter = iter(input.split("\n\n"))

import re
from math import prod

get_numbers = lambda a: list(map(int, re.findall('\d+', a)))


print([get_numbers(next(input_iter).split('\n')[_]) for _ in range(3,6)])




class Monkey:

    def __init__(self,input,divider):
        self.items = get_numbers(next(input_iter).split('\n')[1])
        self.operation = next(input_iter).split('\n')[2].split('=')[1]
        self.test,self.true,self.false = [get_numbers(next(input_iter).split('\n')[_]) for _ in range(3,6)]
        self.divider = divider 
        self.inspections = 0


    def inspect(self,monkeys):
        for item in self.items:
            self.inspection_number += 1
            worry_level = eval(self.operation, {'old':item})//self.divider
            if worry_level % self.test[0]:
                monkeys[self.true[0]].items.append(item)
            else:
                monkeys[self.false[0]].false[0].items.append(item)
        self.items.clear()

            