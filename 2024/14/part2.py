
robots = []
grid_width = 101
grid_height = 103


def add_robot(input):
    global robots

    i = input.replace('p=', '').replace('v=', '').split(' ')
    j = i[0].split(',')
    pos = [int(j[0]), int(j[1])]
    k = i[1].split(',')
    vel = [int(k[0]), int(k[1])]
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

def diff_positions():
    global robots

    seen = set()
    for r in robots:
        this_set = {(r[0][0], r[0][1])}
        if this_set.issubset(seen):
            return False
        else:
            seen.add((r[0][0], r[0][1]))
    return True

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
        result_grid[r[0][1]][r[0][0]] = 'X'
    
    for y in range(len(result_grid)):
        print(''.join(result_grid[y]))

with open("2024/14/input.txt") as fp:
    for line in fp:
        add_robot(line.strip())

# print(robots)
for i in range(10000):
    move_robots()    
    if diff_positions():
        write_grid(i+1)