antennas = dict()
grid = []

with open('2024/08/input.txt') as file:
    for line in file:
        grid.append(line.replace('\n', ''))

for y in range(0, len(grid)):
    for x in range(0, len(grid[y])):
        if grid[y][x] != '.':
            if antennas.get(grid[y][x]) == None:
                antennas[grid[y][x]] = set()
            antennas[grid[y][x]].add((x, y))

for k in antennas.keys():
    for loc1 in antennas.get(k):
        for loc2 in antennas.get(k):
            if loc1[0] == loc2[0] and loc1[1] == loc2[1]:
                continue
            x_dist = loc2[0] - loc1[0]
            y_dist = loc2[1] - loc1[1]
            new_x = loc1[0] - (x_dist)
            new_y = loc1[1] - (y_dist)
            
            while 0 <= new_x and new_x < len(grid[0]) and 0 <= new_y and new_y < len(grid):
                grid[new_y] = grid[new_y][:new_x] + '#' + grid[new_y][new_x+1:]
                new_x -= x_dist
                new_y -= y_dist

antinode_count = 0
for y in range(0, len(grid)):
    print(grid[y])
    antinode_count += len(grid[y]) - grid[y].count('.')
print(str(antinode_count))

# print(str(grid))
# print(str(antennas))
