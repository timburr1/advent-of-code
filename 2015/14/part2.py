
reindeer = []
positions = dict()
points = dict()

def add_reindeer(input):
    global reindeer

    a = input.split(' can fly ')
    name = a[0]
    b = a[1].split(' km/s for ')
    speed = int(b[0])
    c = b[1].split(' seconds, but then must rest for ')
    go_time = int(c[0])
    rest_time = int(c[1].split(' ')[0])

    reindeer.append([name, speed, go_time, rest_time])

def update(positions, t):
    global reindeer, points

    for r in reindeer:
        name = r[0]
        speed = r[1]
        go_time = r[2]
        rest_time = r[3]
        if t % (go_time + rest_time) >= go_time:
            continue
        else:
            positions[name] += speed

    max_pos = -1
    for r in reindeer:
        if positions[r[0]] > max_pos:
            max_pos = positions[r[0]]
    for r in reindeer:
        if positions[r[0]] == max_pos:
            points[r[0]] += 1

    return positions

with open('2015/14/input.txt') as fp:    
    for line in fp:
        add_reindeer(line.strip())

for r in reindeer:
    positions[r[0]] = 0
    points[r[0]] = 0

# print(str(positions))
for t in range(2503): 
    positions = update(positions, t)

max_score = -1
for v in points.values():
    if v > max_score:
        max_score = v
print(str(max_score))
