
x_distance = 0
y_distance = 0

def move(input):
    global x_distance, y_distance

    vals = input.split(' ')
    
    if vals[0] == 'forward':
        x_distance += int(vals[1])
    elif vals[0] == 'up':
        y_distance -= int(vals[1])
        if y_distance < 0:
            y_distance = 0
    else: # down
        y_distance += int(vals[1])

with open('2021/02/input.txt') as fp:
    for line in fp:
        move(line.replace('\n', ''))

print(str(int(x_distance) * int(y_distance)))