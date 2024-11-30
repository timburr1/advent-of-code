
nodes = {}

def add_node(line: str):
    parts = line.split(" = ")
    key = parts[0]
    vals = parts[1].split(", ")
    left = vals[0][1:]
    right = vals[1][:-1]
    nodes[key] = [left, right]
    # print(key + ": [" + left + ", " + right + "]")

with open('input.txt', 'r') as file:
    lines = file.read().splitlines()

directions = lines[0].strip()
# print(directions)

for line in lines[2:]:
    add_node(line)

step_count = 0
idx = 0
this_node = "AAA"
while True:
    if idx >= len(directions):
        idx = 0

    # print(directions[idx])

    if this_node == "ZZZ":
        break
    elif directions[idx] == "L":
        this_node = nodes[this_node][0]
    else: # go right    
        this_node = nodes[this_node][1]

    # print("moving to " + this_node)
    step_count += 1
    idx += 1

print(step_count)