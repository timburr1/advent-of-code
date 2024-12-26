
grid = []

with open('2020/03/input.txt') as fp:
    for line in fp:
        grid.append(line.strip())

c1 = 0
c2 = 0 
c3 = 0 
c4 = 0 
for y in range(len(grid)):
    # right 1, down 1:
    x = (y) % len(grid[y])
    if grid[y][x] == '#':
        c1 += 1

    # right 3, down 1:
    x = (3 * y) % len(grid[y])
    if grid[y][x] == '#':
        c2 += 1

    # right 5, down 1:
    x = (5 * y) % len(grid[y])
    if grid[y][x] == '#':
        c3 += 1

    # right 7, down 1:
    x = (7 * y) % len(grid[y])
    if grid[y][x] == '#':
        c4 += 1

# right 1, down 2:
c5 = 0   
for y in range(0, len(grid), 2):
    x = int(y / 2) % len(grid[y])
    if grid[y][x] == '#':
        c5 += 1

print(str(c1 * c2 * c3 * c4 * c5))
