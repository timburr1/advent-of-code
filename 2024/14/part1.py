
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

def count_and_multiply():
    global grid_height, grid_width, robots

    vals = [0, 0, 0, 0]
    w = int(grid_width / 2)
    h = int(grid_height / 2)
    for r in robots:
        if r[0][0] < w and r[0][1] < h:
            vals[0] += 1
        elif  r[0][0] > w and r[0][1] < h:
            vals[1] += 1
        elif  r[0][0] < w and r[0][1] > h:
            vals[2] += 1
        elif  r[0][0] > w and r[0][1] > h:
            vals[3] += 1

    prod = 1
    for v in vals:
        prod *= v
    return prod

with open("2024/14/input.txt") as fp:
    for line in fp:
        add_robot(line.strip())
# print(robots)
for i in range(100):
    move_robots()
print(count_and_multiply())