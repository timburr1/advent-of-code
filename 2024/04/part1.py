
grid = []

def check_forward(x, y):
    global grid

    if x > len(grid[y]) - 4:
        return False
    else:
        return grid[y][x:x+4] == 'XMAS' 

def check_backward(x, y):
    global grid

    if x < 3:
        return False
    
    for i in range(len('XMAS')):
        if grid[y][x-i] != 'XMAS'[i]:
            return False
        
    return True

def check_up(x, y):
    global grid

    if y < 3:
        return False

    for i in range(len('XMAS')):
        if grid[y-i][x] != 'XMAS'[i]:
            return False
        
    return True

def check_down(x, y):
    global grid

    if y > len(grid) - 4:
        return False

    for i in range(len('XMAS')):
        if grid[y+i][x] != 'XMAS'[i]:
            return False
        
    return True

def check_up_right(x, y):
    global grid

    if x > len(grid[y]) - 4 or y < 3:
        return False

    for i in range(len('XMAS')):
        if grid[y-i][x+i] != 'XMAS'[i]:
            return False 
        
    return True

def check_up_left(x, y):
    global grid

    if x < 3 or y < 3:
        return False

    for i in range(len('XMAS')):
        if grid[y-i][x-i] != 'XMAS'[i]:
            return False 
        
    return True

def check_down_right(x, y):
    global grid

    if x > len(grid[y]) - 4 or y > len(grid) - 4:
        return False

    for i in range(len('XMAS')):
        if grid[y+i][x+i] != 'XMAS'[i]:
            return False
        
    return True

def check_down_left(x, y):
    global grid

    if x < 3 or y > len(grid) - 4:
        return False

    for i in range(len('XMAS')):
        if grid[y+i][x-i] != 'XMAS'[i]:
            return False
        
    return True

with open('2024/04/input.txt') as fp:    
    for line in fp:
        grid.append(line.replace('\n', ''))
        
# print(str(grid))

count = 0

for y in range(0, len(grid)):
    for x in range(0, len(grid[y])):
        if check_forward(x, y):
            count += 1
        if check_backward(x, y):
            count += 1
        if check_up(x, y):
            count += 1
        if check_down(x, y):
            count += 1
        if check_up_right(x, y):
            count += 1
        if check_up_left(x, y):
            count += 1
        if check_down_right(x, y):
            count += 1
        if check_down_left(x, y):
            count += 1

print(str(count))