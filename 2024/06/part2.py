
grid = []
facing = 'N'
x = 0
y = 0

def count_xs():
    global grid
    count = 0
    for b in range(0, len(grid)):
        count += grid[b].count('X')
    return count

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

def move():
    global grid, facing, x, y
    
    grid[y] = grid[y][:x] + 'X' + grid[y][x+1:]
    #print(str(grid))

    if (facing == 'N' and y == 0) or (facing == 'E' and x == len(grid[y])-1) or (facing == 'S' and y == len(grid)-1) or (facing == 'W' and x == 0):
        # reached an edge
        return True
    
    if (facing == 'N' and grid[y-1][x] == '#') or (facing == 'E' and grid[y][x+1] == '#') or (facing == 'S' and grid[y+1][x] == '#') or (facing == 'W' and grid[y][x-1] == '#'):
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
    global grid, x, y
    for b in range(0, len(grid)):
        for a in range(0, len(grid[b])):
            if grid[b][a] == '^':
                x = a
                y = b
                return

with open('2024/06/input.txt') as fp:    
    for line in fp:
        grid.append(line.replace('\n', ''))

# print(str(grid))
init()
# print(str(x) + ', ' + str(y))
done = move()
while not done:
    done = move()
# for y in range(0, len(grid)):
#    print(str(grid[y]))

print(str(count_xs()))
