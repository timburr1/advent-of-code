password = 0
position = 50

with open('2025/01/input.txt') as file:
    for line in file:
        line = line.replace("\n", "")
        # print(line)
        if line.startswith("L"):
            position -= int(line[1:])
        else:
            position += int(line[1:])
        
        position %= 100
        print(str(position))
              
        if position == 0:
            password += 1

print(str(password))