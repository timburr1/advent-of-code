
robots = []
grid_width = 200
grid_height = 50

def add_robot(input):
    global robots

    i = input.replace('position=<', '').split('> velocity=<')
    j = i[0].split(',')
    pos = [int(j[0].strip()), int(j[1].strip())]
    k = i[1].replace('>', '').split(',')
    vel = [int(k[0].strip()), int(k[1].strip())]
    robots.append([pos, vel])

def move_robots():
    global grid_height, grid_width, robots

    for r in robots:
        # update x:
        r[0][0] += r[1][0] 
        if r[0][0] < 0:
            r[0][0] += grid_width
        if r[0][0] >= 0:
            r[0][0] %= grid_width
        # update y:
        r[0][1] += r[1][1] 
        if r[0][1] < 0:
            r[0][1] += grid_height
        if r[0][1] >= 0:
            r[0][1] %= grid_height

def write_grid(t):
    global grid_height, grid_width, robots
    print('\n---------------\n' + str(t) + ':\n')
    
    result_grid = []
    for y in range(grid_height):
        this_row = []
        for x in range(grid_width):
            this_row.append('_')
        result_grid.append(this_row)

    for r in robots:
        result_grid[r[0][1] % grid_height][r[0][0] % grid_width] = 'X'
    
    for y in range(len(result_grid)):
        print(''.join(result_grid[y]))

with open("2018/10/input.txt") as fp:
    for line in fp:
        add_robot(line.strip())

i = 25

while True:
    move_robots()    
    write_grid(i+1)
    input('next')
    i += 1