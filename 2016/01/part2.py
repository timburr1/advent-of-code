
directions = []
facing = 'N'
current_x = 0
current_y = 0
visited = [[False for x in range(1000)] for y in range(1000)]
visited [500][500] = True

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
    OFFSET = 500

    if instruction.startswith('R'):
        turn_right()
    else: # L
        turn_left()
    
    distance = int(instruction[1:])

    if facing == 'N':
        for i in range(distance):
            current_y += 1
            if visited[current_x + OFFSET][current_y + OFFSET] == True:
                print(str(abs(current_x) + abs(current_y)))
                return
            else:
                visited[current_x + OFFSET][current_y + OFFSET] = True
    elif facing == 'E':
        for i in range(distance):
            current_x += 1
            if visited[current_x + OFFSET][current_y + OFFSET] == True:
                print(str(abs(current_x) + abs(current_y)))
                return
            else:
                visited[current_x + OFFSET][current_y + OFFSET] = True
    elif facing == 'S':
        for i in range(distance):
            current_y -= 1
            if visited[current_x + OFFSET][current_y + OFFSET] == True:
                print(str(abs(current_x) + abs(current_y)))
                return
            else:
                visited[current_x + OFFSET][current_y + OFFSET] = True
    else: # W
        for i in range(distance):
            current_x -= 1
            if visited[current_x + OFFSET][current_y + OFFSET] == True:
                print(str(abs(current_x) + abs(current_y)))
                return
            else:
                visited[current_x + OFFSET][current_y + OFFSET] = True
    
    #print(str(visited))

with open('2016/01/input.txt') as fp:
    for line in fp:
        for dir in line.split(', '):
            directions.append(dir)

for dir in directions:
    move(dir)
