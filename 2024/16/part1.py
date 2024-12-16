
grid = []
start_location = (-1, -1)
end_location = (-1, -1)

def update_grid(input):
    global grid, start_location, end_location

    this_row = []
    for i in range(len(input)):
        this_row.append(input[i])
        if input[i] == 'S':
            start_location = (i, len(grid))
        elif input[i] == 'E':
            end_location = (i, len(grid)) 
    grid.append(this_row)

def left(f):
    if f == 'up':
        return 'left'
    if f == 'down':
        return 'right'
    if f == 'left':
        return 'down'
    if f == 'right':
        return 'up'

def right(f):
    if f == 'up':
        return 'right'
    if f == 'down':
        return 'left'
    if f == 'left':
        return 'up'
    if f == 'right':
        return 'down'

def can_move_forward(position, facing):
    global grid
    
    x = position[0]
    y = position[1]
    
    if facing == 'up':
        return grid[y-1][x] != '#'
    if facing == 'down':
        return grid[y+1][x] != '#'
    if facing == 'left':
        return grid[y][x-1] != '#'
    if facing == 'right':
        return grid[y][x+1] != '#'

def move(position, facing):

    x = position[0]
    y = position[1]
    
    if facing == 'up':
        return (x, y-1)
    if facing == 'down':
        return (x, y+1)
    if facing == 'left':
        return (x-1, y)
    if facing == 'right':
        return (x+1, y)
    
def search(start, end, facing, cost):
    
    if start[0] == end[0] and start[1] == end[1]:
        return cost
    
    if can_move_forward(start, facing):
        # move forward, turn right, turn left
        return min(search(move(start, facing), end, facing, cost+1), search(start, end, left(facing), cost + 1000), search(start, end, right(facing), cost + 1000))
    elif not can_move_forward(start, left(facing)) and not can_move_forward(start, left(facing)):
        return 1000000 # max value, we hit a dead end
    # turn right, turn left
    return min(search(start, end, left(facing), cost + 1000), search(start, end, right(facing), cost + 1000))
    
with open("2024/16/test.txt") as fp:
    for line in fp:
        update_grid(line.strip())

# for row in grid:
#     print(''.join(row))
# print('Start at ' + str(start_location))
# print('Looking for ' + str(end_location))

dist = search(start_location, end_location, 'right', 0)
print(dist)

# test: 7036
# test2: 11048
