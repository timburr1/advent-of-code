
grid = []
robot_x = -1
robot_y = -1

def move_up():
    global grid, robot_x, robot_y

    if grid[robot_y-1][robot_x] == '.':
        grid[robot_y][robot_x] = '.'
        robot_y -= 1
        grid[robot_y][robot_x] = '@'
        return

    for i in range(robot_y-1, 0, -1):
        if grid[i][robot_x] == '#':
            return
        elif grid[i][robot_x] == '.':
            for j in range(i, robot_y):
                grid[j][robot_x] = grid[j+1][robot_x]
            
            grid[robot_y][robot_x] = '.'
            robot_y -= 1
            grid[robot_y][robot_x] = '@'
            return    

def move_down():
    global grid, robot_x, robot_y

    if grid[robot_y+1][robot_x] == '.':
        grid[robot_y][robot_x] = '.'
        robot_y += 1
        grid[robot_y][robot_x] = '@'
        return 
    
    for i in range(robot_y+1, len(grid)):
        if grid[i][robot_x] == '#':
            return
        elif grid[i][robot_x] == '.':
            for j in range(i, robot_y, -1):
                grid[j][robot_x] = grid[j-1][robot_x]
            
            grid[robot_y][robot_x] = '.'
            robot_y += 1
            grid[robot_y][robot_x] = '@'
            return

def move_left():
    global grid, robot_x, robot_y

    if grid[robot_y][robot_x-1] == '.':
        grid[robot_y][robot_x] = '.'
        robot_x -= 1
        grid[robot_y][robot_x] = '@'
        return

    for i in range(robot_x-1, 0, -1):
        if grid[robot_y][i] == '#':
            return
        elif grid[robot_y][i] == '.':
            for j in range(i, robot_x):
                grid[robot_y][j] = grid[robot_y][j+1]
            
            grid[robot_y][robot_x] = '.'
            robot_x -= 1
            grid[robot_y][robot_x] = '@'
            return

def move_right():
    global grid, robot_x, robot_y

    if grid[robot_y][robot_x+1] == '.':
        grid[robot_y][robot_x] = '.'
        robot_x += 1
        grid[robot_y][robot_x] = '@'
        return

    for i in range(robot_x+1, len(grid[robot_y])):
        if grid[robot_y][i] == '#':
            return
        elif grid[robot_y][i] == '.':
            for j in range(i, robot_x, -1):
                grid[robot_y][j] = grid[robot_y][j-1]
            
            grid[robot_y][robot_x] = '.'
            robot_x += 1
            grid[robot_y][robot_x] = '@'
            return

def move_robot(input):
    for c in input:
        # print('Move ' + c)
        if c == '^':
            move_up()
        elif c == 'v':
            move_down()
        elif c == '<':
            move_left()
        elif c == '>':
            move_right()

        # for row in grid:
        #     print(''.join(row))
        # print('\n')

def update_grid(line):
    global grid, robot_x, robot_y

    i = line.find('@')
    if i > -1:
        robot_x = i
        robot_y = len(grid)
        # print('Found robot at ' + str(robot_x) + ', ' + str(robot_y))
    grid.append(list(line))

def sum_boxes():
    global grid

    sum = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 'O':
                sum += y * 100 + x
    return sum

with open("2024/15/input.txt") as fp:
    for line in fp:
        if line == '\n':
            continue
        elif line.count('^') > 0:
            move_robot(line.strip())
        else:
            update_grid(line.strip())
        #print(line.strip())

print(sum_boxes())
