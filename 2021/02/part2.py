
aim = 0
x_distance = 0
y_distance = 0

def move(input):
    global aim, x_distance, y_distance

    vals = input.split(' ')
            
    if vals[0] == 'down':   
        aim += int(vals[1])
    elif vals[0] == 'up':
        aim -= int(vals[1])
    else: # forward
        x_distance += int(vals[1])
        y_distance += aim * int(vals[1])

with open('2021/02/input.txt') as fp:
    for line in fp:
        move(line.replace('\n', ''))

print(str(int(x_distance) * int(y_distance)))