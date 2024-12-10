
grid = []
trailheads = []
peaks = []

def score(start):
    global grid

    x = start[0]
    y = start[1]

    if grid[y][x] == 9:
        return 1
    
    if x >= len(grid[0]) or y >= len(grid):
        return 0

    sum = 0
    if x > 0:
        if grid[y][x-1] == grid[y][x]+1:
            sum += score((x-1, y))
    if y > 0:
        if grid[y-1][x] == grid[y][x]+1:
            sum += score((x, y-1))
    if y < len(grid)-1:
        if grid[y+1][x] == grid[y][x]+1:
            sum += score((x, y+1))
    if x < len(grid[y])-1:
        if grid[y][x+1] == grid[y][x]+1:
            sum += score((x+1, y))
    return sum

with open('2024/10/input.txt') as fp:
    y = 0
    for line in fp:
        # print(line.replace('\n', ''))
        this_row = []
        for x in range(0, len(line.replace('\n', ''))):
            if line[x] == '0':
                trailheads.append((x, y))
#            if line[x] == '9':
#                peaks.append((x, y))
            this_row.append(int(line[x]))
        y += 1
        grid.append(this_row)

print(str(grid))
print(str(trailheads))
# print(str(peaks))

sum = 0
for t in trailheads:
    sum += score(t)
print(str(sum))
