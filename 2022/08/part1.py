
grid = []

def check_up(x, y):
    global grid
    for i in range(y-1, -1, -1):
        if grid[i][x] >= grid[y][x]:
            return False
    return True
    
def check_down(x, y):
    global grid
    for i in range(y+1, len(grid)):
        if grid[i][x] >= grid[y][x]:
            return False
    return True

def check_left(x, y):
    global grid
    for i in range(x-1, -1, -1):
        if grid[y][i] >= grid[y][x]:
            return False
    return True

def check_right(x, y):
    global grid
    for i in range(x+1, len(grid[0])):
        if grid[y][i] >= grid[y][x]:
            return False
    return True

def check_tree(x, y):
    return check_up(x,y) or check_down(x,y) or check_left(x,y) or check_right(x,y)

with open('2022/08/input.txt') as fp:    
    for line in fp:
        this_row = []
        for c in line.strip():
            this_row.append(int(c))
        grid.append(this_row)

# print(str(grid))

count = 2 * len(grid) + 2 * len(grid[0]) - 4

for y in range(1, len(grid) - 1):
    for x in range(1, len(grid[0]) - 1):
        if check_tree(x, y):
            count += 1

print(str(count))
