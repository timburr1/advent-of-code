
grid = []
this_grid = []
visited = {}
facing = 'N'
start_x = 0
start_y = 0
x = 0
y = 0

def check_obstacle_location(a, b):
    global grid, this_grid, facing, start_x, x, start_y, y, visited

    if grid[b][a] == '#':
        # there is already an obstacle here
        return False

    this_grid = grid.copy()
    this_grid[b] = this_grid[b][:a] + '#' + this_grid[b][a+1:]
    
    visited = {}
    facing = 'N'
    x = start_x
    y = start_y

    m = move()
    while not m:
        if visited.get((x,y)) != None and {facing} <= visited.get((x, y)):
            return True
        m = move()
        
    return False

def rotate():
    global facing
    if facing == 'N':
        facing = 'E'
    elif facing == 'E':
        facing = 'S'
    elif facing == 'S':
        facing = 'W'
    else: # W
        facing = 'N'

def visit(x, y, f):
    global visited

    if visited.get((x,y)) == None:
        visited[(x,y)] = {f}
    else:
        visited[(x,y)].add(f)

def move():
    global this_grid, visited, facing, x, y
    
    visit(x, y, facing)

    if (facing == 'N' and y == 0) or (facing == 'E' and x == len(this_grid[y])-1) or (facing == 'S' and y == len(this_grid)-1) or (facing == 'W' and x == 0):
        # reached an edge
        return True
    
    if (facing == 'N' and this_grid[y-1][x] == '#') or (facing == 'E' and this_grid[y][x+1] == '#') or (facing == 'S' and this_grid[y+1][x] == '#') or (facing == 'W' and this_grid[y][x-1] == '#'):
        rotate()
    else:   
        if facing == 'N':
            y -= 1
        elif facing == 'E':
            x += 1
        elif facing == 'S':
            y += 1
        elif facing == 'W':
            x -= 1
    
    return False

def init():
    global grid, start_x, start_y
    for b in range(0, len(grid)):
        for a in range(0, len(grid[b])):
            if grid[b][a] == '^':
                start_x = a
                start_y = b
                return

with open('2024/06/test.txt') as fp:    
    for line in fp:
        grid.append(line.replace('\n', ''))

init()

count = 0
for b in range(0, len(grid)):
    for a in range(0, len(grid[b])):
        if check_obstacle_location(a, b) :
            count += 1
print(str(count))
