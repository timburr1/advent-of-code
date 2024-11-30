
def elevate(string):
    current_floor = 0

    for i in range(len(string)):
        if(string[i] == '('):
            current_floor += 1
        elif(string[i] == ')'):
            current_floor -= 1
    print(current_floor)
     

with open('input.txt') as fp:
    for line in fp:
        elevate(line)