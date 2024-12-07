
universe = []

with open('2023/11/test.txt') as file:
    for line in file:
        # print(line.replace('\n', ''))
        universe.append(line.replace('\n', ''))
        if line.count('#') == 0:
            for i in range(0, 1000000):
                universe.append('.' * len(universe[0]))

i = 0
while i < len(universe[0]):
    if '#' not in [line[i] for line in universe]:
        for j in range(len(universe)):
            universe[j] = universe[j][:i] + ('.' * 1000000) + universe[j][i:]
        i += 1
    i += 1            

galaxies = []

for y in range(0, len(universe)):
    for x in range(0, len(universe[y])):
        if universe[y][x] == '#':
            galaxies.append((x, y))

total_dist = 0
for a in range(0, len(galaxies)-1):
    for b in range(a+1, len(galaxies)):
        total_dist += abs(galaxies[a][0] - galaxies[b][0])
        total_dist += abs(galaxies[a][1] - galaxies[b][1])

print(str(total_dist))
