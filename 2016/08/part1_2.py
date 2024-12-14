
screen_width = 50
screen_height = 6
screen = []

def draw_rect(w, h):
    global screen

    for y in range(h):
        for x in range(w):
            screen[y][x] = '#'

def rotate_row(row, num):
    global screen, screen_width
    screen[row] = screen[row][-num:] + screen[row][:-num]

def rotate_col(col, num):
    global screen, screen_height

    new_col = []
    for y in range(screen_height):
        new_col.append(screen[y][col])
    new_col = new_col[-num:] + new_col[:-num]
    for i in range(len(new_col)):
        screen[i][col] = new_col[i]

def exec(instruction):
    if instruction.startswith('rect'):
        i = instruction.replace('rect ', '').split('x')
        draw_rect(int(i[0]), int(i[1]))
    elif instruction.startswith('rotate row'):
        i = instruction.replace('rotate row y=', '').split(' by ')
        rotate_row(int(i[0]), int(i[1]))
    elif instruction.startswith('rotate column'):
        i = instruction.replace('rotate column x=', '').split(' by ')
        rotate_col(int(i[0]), int(i[1]))

def print_screen():
    global screen

    for y in range(len(screen)):
        print(''.join(screen[y]))
    print('\n')

for y in range(screen_height):
    this_row = []
    for x in range(screen_width):
        this_row.append('.')
    screen.append(this_row)

with open("2016/08/input.txt") as fp:
    for line in fp:
        exec(line.strip())
        print_screen()

count = 0
for y in range(screen_height):
    for x in range(screen_width):
        if screen[y][x] == '#':
            count += 1
print(count)
