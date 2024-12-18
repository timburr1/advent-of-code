
grid = []

def update_grid(line):
    global grid

    l = line.split(' @ ')
    s = l[1].split(': ')
    pos = (s[0].split(','))
    start_x = int(pos[0])
    start_y = int(pos[1])
    size = (s[1].split('x'))
    width = int(size[0])
    height = int(size[1])

    for y in range(start_y, start_y + height):
        for x in range(start_x, start_x + width):
            if grid[y][x] == '.':
                grid[y][x] = '#'
            elif grid[y][x] == '#':
                grid[y][x] = 'x'

for i in range(1000):
    this_row = []
    for j in range(1000):
        this_row.append('.')
    grid.append(this_row)

with open('2018/03/input.txt') as fp:
    for line in fp:
        update_grid(line.strip())

c = 0
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] == 'x':
            c += 1
print(c)