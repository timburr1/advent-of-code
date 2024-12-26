
grid = []

def init_grid():
    global grid

    for y in range(999):
        this_row =[]
        for x in range(999):
            this_row.append(0)
        grid.append(this_row)

def draw_line(x1, y1, x2, y2):
    global grid

    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2)+1):
            grid[y][x1] += 1
    elif y1 == y2:
        for x in range(min(x1, x2), max(x1, x2)+1):
            grid[y1][x] += 1
    else:
        return 

init_grid()

with open('2021/05/input.txt') as fp:
    for line in fp:
        coords = line.strip().split(' -> ')
        start = coords[0].split(',')
        end = coords[1].split(',')

        draw_line(int(start[0]), int(start[1]), int(end[0]), int(end[1]))

c = 0
for y in range(len(grid)):
    s = ''
    for x in range(len(grid[y])):
        s += str(grid[y][x])
        if grid[y][x] > 1:
            c += 1
    print(s)
print(c)