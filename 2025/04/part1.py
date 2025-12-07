grid = []

with open('2025/04/input.txt') as file:
    for line in file:
        line = line.replace("\n", "")
        # print(line)
        # populate grid
        grid.append(line)

def is_accessible(x_in, y_in):
    global grid

    # count adjacent '@' symbols
    count = 0    
    for y in range(max(y_in-1, 0), min(y_in+2, len(grid))):
        for x in range(max(x_in-1, 0), min(x_in+2, len(grid[0]))):
            if x == x_in and y == y_in:
                continue

            if grid[y][x] == '@':
                count += 1                
                if count >= 4:
                    return False          
    # print("found accessible roll at " + str(x_in) + ", " + str(y_in))
    return True

count = 0
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == '@' and is_accessible(x, y):
            count += 1

print(str(count))