
RED_CUBES = 12
GREEN_CUBES = 13
BLUE_CUBES = 14

# return game number if game is possible
# 0 otherwise
def checkGame(line):
    pieces = line.split(":")
    game_num = int(pieces[0].replace("Game ", ""))
    reveals = pieces[1].split(";")

    # red_cubes_revealed = 0
    # green_cubes_revealed = 0
    # blue_cubes_revealed = 0
    
    for r in reveals:
        red_cubes_revealed = 0
        green_cubes_revealed = 0
        blue_cubes_revealed = 0
        
        cubes = r.split(",")
        # print(items)
        for i in range(0, len(cubes)):
            tokens = cubes[i].split(" ")
            print(tokens)

            if tokens[2].strip() == "red":
                # print(tokens[1] + " red")
                red_cubes_revealed += int(tokens[1])
            elif tokens[2].strip() == "green":
                # print(tokens[1] + " green")
                green_cubes_revealed += int(tokens[1])
            elif tokens[2].strip() == "blue":
                # print(tokens[1] + " blue")
                blue_cubes_revealed += int(tokens[1])

        if red_cubes_revealed > RED_CUBES or blue_cubes_revealed > BLUE_CUBES or green_cubes_revealed > GREEN_CUBES:
            # print(str(game_num) + " INVALID")        
            return 0

    # print(str(game_num) + " is valid")
    return game_num

sum = 0

with open('input.txt') as fp:
    for line in fp:
        # print(line)
        sum += checkGame(line)
        
print(str(sum))