
grid = []
robot_x = -1
robot_y = -1

def move_up():
    global grid, robot_x, robot_y

    global grid, robot_x, robot_y

    # todo
    return

def move_down():
    global grid, robot_x, robot_y

    global grid, robot_x, robot_y

    # todo
    return

def move_left():
    global grid, robot_x, robot_y

    # todo
    return

def move_right():
    global grid, robot_x, robot_y

    # todo
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

def expand_grid():
    global grid, robot_x, robot_y

    new_grid = []
    for y in range(len(grid)):
        this_line = []
        for x in range(len(grid[0])):
            if grid[y][x] == '#':
                this_line += ['#', '#']
            elif grid[y][x] == 'O':
                this_line += ['[', ']']
            elif grid[y][x] == '.':
                this_line += ['.', '.']
            elif grid[y][x] == '@':
                this_line += ['@', '.']
                robot_y = y
                robot_x 
        new_grid.append(this_line)
    grid = new_grid

def sum_boxes():
    global grid

    sum = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 'O':
                sum += y * 100 + x
    return sum

with open("2024/15/test3.txt") as fp:
    for line in fp:
        if line == '\n':
            expand_grid()
        elif line.count('^') > 0:
            move_robot(line.strip())
        else:
            grid.append(list(line.strip()))
        #print(line.strip())

# print(sum_boxes())
# for row in grid:
#     print(''.join(row))