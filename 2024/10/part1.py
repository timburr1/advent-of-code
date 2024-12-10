
grid = []
trailheads = []
peaks = []

def can_reach(start, target):
    global grid

    x = start[0]
    y = start[1]

    if x == target[0] and y == target[1]:
        return True
    
    if x >= len(grid[0]) or y >= len(grid):
        return False

    path_exists = False
    if x > 0:
        if grid[y][x-1] == grid[y][x]+1:
            path_exists = path_exists or can_reach((x-1, y), target)
    if y > 0:
        if grid[y-1][x] == grid[y][x]+1:
            path_exists = path_exists or can_reach((x, y-1), target)
    if y < len(grid)-1:
        if grid[y+1][x] == grid[y][x]+1:
            path_exists = path_exists or can_reach((x, y+1), target)
    if x < len(grid[y])-1:
        if grid[y][x+1] == grid[y][x]+1:
            path_exists = path_exists or can_reach((x+1, y), target)
    return path_exists

with open('2024/10/input.txt') as fp:
    y = 0
    for line in fp:
        # print(line.replace('\n', ''))
        this_row = []
        for x in range(0, len(line.replace('\n', ''))):
            if line[x] == '0':
                trailheads.append((x, y))
            if line[x] == '9':
                peaks.append((x, y))
            this_row.append(int(line[x]))
        y += 1
        grid.append(this_row)

# print(str(grid))
# print(str(trailheads))
# print(str(peaks))

sum = 0
for t in trailheads:
    for p in peaks:
        if can_reach(t, p):
            sum += 1
print(str(sum))
