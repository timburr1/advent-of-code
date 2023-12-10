
def turn_on(coord_str):
    coords = coord_str.split(" through ")
    start = coords[0].split(",")
    x_min = int(start[0])
    y_min = int(start[1])
    end = coords[1].split(",")
    x_max = int(end[0])
    y_max = int(end[1])

    for x in range(x_min, x_max + 1):
        for y in range(y_min, y_max + 1):
            grid[x][y] = True

def turn_off(coord_str):
    coords = coord_str.split(" through ")
    start = coords[0].split(",")
    x_min = int(start[0])
    y_min = int(start[1])
    end = coords[1].split(",")
    x_max = int(end[0])
    y_max = int(end[1])

    for x in range(x_min, x_max + 1):
        for y in range(y_min, y_max + 1):
            grid[x][y] = False

def toggle(coord_str):
    coords = coord_str.split(" through ")
    start = coords[0].split(",")
    x_min = int(start[0])
    y_min = int(start[1])
    end = coords[1].split(",")
    x_max = int(end[0])
    y_max = int(end[1])

    for x in range(x_min, x_max + 1):
        for y in range(y_min, y_max + 1):
            grid[x][y] = not grid[x][y]

def execute(line):
    if line.startswith("turn on "):
        turn_on(line.replace("turn on ", ""))
    elif line.startswith("turn off"):
        turn_off(line.replace("turn off ", ""))
    else: # toggle
        toggle(line.replace("toggle ", ""))

def initialize_grid():
    global grid 
    grid = []

    for i in range(1000):
        this_row = []
        for j in range(1000):
            this_row.append(False)
        grid.append(this_row)

def count_lights():
    count = 0

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y]:
                count += 1

    print(count)

initialize_grid()

with open("input.txt") as fp:
    for line in fp:
        execute(line.strip())

count_lights()