
directions = []
facing = 'N'
x_dist_travelled = 0
y_dist_travelled = 0

def turn_right():
    global facing
    
    if facing == 'N':
        facing = 'E'
    elif facing == 'E':
        facing = 'S'
    elif facing == 'S':
        facing = 'W'
    else: # W
        facing = 'N'

def turn_left():
    global facing
    
    if facing == 'N':
        facing = 'W'
    elif facing == 'E':
        facing = 'N'
    elif facing == 'S':
        facing = 'E'
    else: # W
        facing = 'S'

def move(instruction):
    global x_dist_travelled, y_dist_travelled

    if instruction.startswith('R'):
        turn_right()
    else: # L
        turn_left()
    
    distance = int(instruction[1:])

    if facing == 'N':
        y_dist_travelled += distance
    elif facing == 'E':
        x_dist_travelled += distance
    elif facing == 'S':
        y_dist_travelled -= distance
    else: # W
        x_dist_travelled -= distance

with open('2016/01/input.txt') as fp:
    for line in fp:
        for dir in line.split(', '):
            directions.append(dir)

for dir in directions:
    move(dir)

# print('x distance: ' + str(x_dist_travelled))
# print('y distance: ' + str(y_dist_travelled))

total_distance = abs(x_dist_travelled) + abs(y_dist_travelled)

print(str(total_distance))
