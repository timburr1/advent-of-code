password = 0
position = 50

with open('2025/01/input.txt') as file:
    for line in file:
        line = line.replace("\n", "")
        val = int(line[1:])

        if line.startswith("L"):
            for i in range(0, val):
                position -= 1
                position %= 100
                if position == 0:
                    password += 1
        else:
            for i in range(0, val):
                position += 1
                position %= 100
                if position == 0:
                    password += 1   
        # print(str(position) + ", " + str(password))
              
        #if position == 0:
        #    password += 1

print(str(password))