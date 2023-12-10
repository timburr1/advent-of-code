
race_times = []
race_distances = []

def parse_times(line):
    line = line.replace("Time:", "").strip()
    times = line.split(" ")    
    for t in times:
        if t != '' and t != " ":
            race_times.append(int(t))

def parse_distances(line):
    line = line.replace("Distance:", "").strip()
    dist = line.split(" ")    
    for d in dist:
        if d != '' and d != " ":
            race_distances.append(int(d))

def parse(line):
    if(line.startswith("Time:")):
        parse_times(line)
    else:
        parse_distances(line)

def calculate_distance(hold_time, total_time):
    return hold_time * (total_time - hold_time)

def count_winning_strats(race_time, distance_to_beat):
    winning_strats = 0
    for i in range(1, race_time):
        if calculate_distance(i, race_time) > distance_to_beat:
            winning_strats += 1
    return winning_strats

with open('input.txt') as fp:
    for line in fp:
        parse(line.strip())

product = 1
for i in range(len(race_times)):
    product *= count_winning_strats(race_times[i], race_distances[i])

print(product)