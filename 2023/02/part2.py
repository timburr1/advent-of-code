
# return the "power" of the game:
# What is the fewest number of cubes of each color that could have been in the bag to make the game possible?
# The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together
def checkGame(line):
    pieces = line.split(":")
    reveals = pieces[1].split(";")

    min_red_cubes = 0
    min_green_cubes = 0
    min_blue_cubes = 0
    
    for r in reveals:
        red_cubes_revealed = 0
        green_cubes_revealed = 0
        blue_cubes_revealed = 0
        
        cubes = r.split(",")
        # print(items)
        for i in range(0, len(cubes)):
            tokens = cubes[i].split(" ")
            # print(tokens)

            if tokens[2].strip() == "red":
                # print(tokens[1] + " red")
                red_cubes_revealed += int(tokens[1])
            elif tokens[2].strip() == "green":
                # print(tokens[1] + " green")
                green_cubes_revealed += int(tokens[1])
            elif tokens[2].strip() == "blue":
                # print(tokens[1] + " blue")
                blue_cubes_revealed += int(tokens[1])

        if red_cubes_revealed > min_red_cubes:
            min_red_cubes = red_cubes_revealed    
        if green_cubes_revealed > min_green_cubes:
            min_green_cubes = green_cubes_revealed
        if blue_cubes_revealed > min_blue_cubes:
            min_blue_cubes = blue_cubes_revealed
        
    return min_red_cubes * min_green_cubes * min_blue_cubes

sum = 0

with open('input.txt') as fp:
    for line in fp:
        # print(line)
        sum += checkGame(line)
        
print(str(sum))