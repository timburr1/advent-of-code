
def parse_times(line):
    line = line.replace("Time:", "").replace(" ", "")
    global race_time 
    race_time = int(line)
    print("Time: " + str(race_time))

def parse_distances(line):
    line = line.replace("Distance:", "").replace(" ", "")
    global race_distance
    race_distance = int(line)
    print("Distance: " + str(race_distance))

def parse(line):
    if(line.startswith("Time:")):
        parse_times(line)
    else:
        parse_distances(line)

def calculate_distance(hold_time, total_time):
    return hold_time * (total_time - hold_time)

def count_winning_strats():
    winning_strats = 0
    for i in range(1, race_time):
        if calculate_distance(i, race_time) > race_distance:
            winning_strats += 1
    return winning_strats

with open('input.txt') as fp:
    for line in fp:
        parse(line.strip())

print(str(count_winning_strats()))
