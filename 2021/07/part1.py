
positions = []
min_p = 10000
max_p = -1

with open('2021/07/input.txt') as fp:
    for line in fp:
        #print(line.strip())
        for p in line.strip().split(','):
            if int(p) > max_p:
                max_p = int(p)
            if int(p) < min_p:
                min_p = int(p)
            positions.append(int(p))

min_total_dist = 1000000000
for i in range(min_p, max_p+1):
    total_dist = 0
    for p in positions:
        total_dist += abs(p - i)
    if total_dist < min_total_dist:
        min_total_dist = total_dist
print(min_total_dist)