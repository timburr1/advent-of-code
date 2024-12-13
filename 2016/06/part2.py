
grid = []

with open("2016/06/input.txt") as fp:
    for line in fp:
        grid.append(line.strip())
# print(str(grid))

result = ''
for i in range(len(grid[0])):
    counts = dict()
    for j in range(len(grid)):
        if counts.get(grid[j][i]) == None:
            counts[grid[j][i]] = 1
        else:
            counts[grid[j][i]] += 1
    
    min_count = 699
    char = ''
    for k, v in counts.items():
        if v < min_count:
            char = k
            min_count = v
    result += char
print(result)