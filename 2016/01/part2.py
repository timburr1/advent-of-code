
directions = []
facing = 'N'
current_x = 0
current_y = 0
visited = {}

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
    global current_x, current_y, visited

    if instruction.startswith('R'):
        turn_right()
    else: # L
        turn_left()
    
    distance = int(instruction[1:])

    if facing == 'N':
        current_y += distance
    elif facing == 'E':
        current_x += distance
    elif facing == 'S':
        current_y -= distance
    else: # W
        current_x -= distance
    
    key = str(current_x) + ', ' + str(current_y)

    if visited.get(key, False) == True:
        print(str(abs(current_x) + abs(current_y)))
    else:
        visited[key] = True
        print(str(visited))

with open('2016/01/test4.txt') as fp:
    for line in fp:
        for dir in line.split(', '):
            directions.append(dir)

for dir in directions:
    move(dir)

# print('x distance: ' + str(x_dist_travelled))
# print('y distance: ' + str(y_dist_travelled))

#total_distance = abs(x_dist_travelled) + abs(y_dist_travelled)
#print(str(total_distance))
