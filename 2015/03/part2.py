
def visit(line):
    visited = {"0,0"}
    santa_location = (0, 0)
    
    for i in range(len(line)):
        if line[i] == "^":
            santa_location = (santa_location[0], santa_location[1] + 1)
        elif line[i] == "v":
            santa_location = (santa_location[0], santa_location[1] - 1)
        elif line[i] == "<":
            santa_location = (santa_location[0] - 1, santa_location[1])
        else: # >
            santa_location = (santa_location[0] + 1, santa_location[1])

        thisKey = str(santa_location[0]) + "," + str(santa_location[1])
        visited.add(thisKey)
    
    #print(visited)
    print(len(visited))

with open("input.txt") as fp:
    for line in fp:
        visit(line)
