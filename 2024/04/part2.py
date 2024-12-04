
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

def check_for_x(x, y):
    global grid

    if grid[y][x] != 'A':
        return False
    
    # M M
    #  A
    # S S
    if grid[y-1][x-1] == 'M' and grid[y-1][x+1] == 'M':
        return grid[y+1][x-1] == 'S' and grid[y+1][x+1] == 'S'

    # S S
    #  A
    # M M    
    if grid[y+1][x-1] == 'M' and grid[y+1][x+1] == 'M':
        return grid[y-1][x-1] == 'S' and grid[y-1][x+1] == 'S'
    
    # M S
    #  A
    # M S
    if grid[y-1][x-1] == 'M' and grid[y+1][x-1] == 'M':
        return grid[y-1][x+1] == 'S' and grid[y+1][x+1] == 'S'
    
    # S M
    #  A
    # S M
    if grid[y-1][x+1] == 'M' and grid[y+1][x+1] == 'M':
        return grid[y+1][x-1] == 'S' and grid[y-1][x-1] == 'S'
    
    return False

with open('2024/04/input.txt') as fp:    
    for line in fp:
        grid.append(line.replace('\n', ''))
        
# print(str(grid))

count = 0

for y in range(1, len(grid)-1):
    for x in range(1, len(grid[y])-1):
        if check_for_x(x, y):
            count += 1

print(str(count))