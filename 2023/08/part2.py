
nodes = {}
curr_nodes = []

def add_node(line: str):
    parts = line.split(" = ")
    key = parts[0]
    vals = parts[1].split(", ")
    left = vals[0][1:]
    right = vals[1][:-1]
    nodes[key] = [left, right]
    # print(key + ": [" + left + ", " + right + "]")
    if key[2] == "A":
        # print("^ ghost node")
        curr_nodes.append(key)

with open('input.txt', 'r') as file:
    lines = file.read().splitlines()

directions = lines[0].strip()
# print(directions)

for line in lines[2:]:
    add_node(line)

print(curr_nodes)

step_count = 0
idx = 0
while True:
    if idx >= len(directions):
        idx = 0

    print(directions[idx])
    for i in range(len(curr_nodes)):
        if directions[idx] == "L":
            curr_nodes[i] = nodes[curr_nodes[i]][0]
        else: # go right    
            curr_nodes[i] = nodes[curr_nodes[i]][1]
         
    print(curr_nodes)

    step_count += 1
    idx += 1

    done = True
    for node in curr_nodes:
        if node[2] != "Z":
            done = False
            break
    if done:
        break

print(step_count)