forest = []

with open('input_day8.txt','r') as f:
    for line in f:
        forest.append(list(line.strip()))

cols = len(forest[:][1])
rows = len(forest)

def up(forest,row,col):
    row_up = row-1
    i = 0
    while row_up>=0:
        #print(f'comparison: forest[{row}][{col}]: {forest[row][col]} and forest[{row_up}][{col}] {forest[row_up][col]} gives:')
        i+=1
        if forest[row][col]<=forest[row_up][col]:
            return i
        row_up = row_up-1
    return i

def down(forest,row,col):
    row_down = row+1
    i = 0
    while row_down<rows:
        i+=1
        #print(f'comparison: forest[{row}][{col}]: {forest[row][col]} and forest[{row_down}][{col}] {forest[row_down][col]} gives:')
        if forest[row][col] <= forest[row_down][col]:
            return i
        row_down = row_down + 1
    return i

def left(forest,row,col):
    col_left = col-1
    i=0
    while col_left>=0:
        i+=1
        #print(f'comparison: forest[{row}][{col}]: {forest[row][col]} and forest[{row}][{col_left}] {forest[row][col_left]} gives:')
        if forest[row][col]<=forest[row][col_left]:
            return i
        col_left = col_left -1
    return i

def right(forest,row,col):
    col_right = col+1
    i=0
    while col_right<cols:
        i+=1
        #print(f'comparison: forest[{row}][{col}]: {forest[row][col]} and forest[{row}][{col_right}] {forest[row][col_right]} gives:')
        if forest[row][col]<=forest[row][col_right]:
            return i
        col_right = col_right +1
    return i

max_scenic_score = 0
for row in range(0,rows):
    
    for col in range(0,cols):
        
        up_score = up(forest,row,col)
        down_score = down(forest,row,col)
        left_score = left(forest,row,col) 
        right_score = right(forest,row,col) 
        scenic_score = up_score*down_score*left_score*right_score
        if scenic_score>max_scenic_score:
            max_scenic_score = scenic_score
    

print(max_scenic_score)


        



