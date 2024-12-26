
grid = []

with open('2020/03/input.txt') as fp:
    for line in fp:
        grid.append(line.strip())
    
# for r in grid:
#    print(r)

c = 0
for y in range(len(grid)):
    x = (3 * y) % len(grid[y])
    if grid[y][x] == '#':
        c += 1
print(c)
