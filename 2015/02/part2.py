
def calculate_ribbon_length(string):
    side_lengths = string.split('x')
    side0 = int(side_lengths[0])
    side1 = int(side_lengths[1])
    side2 = int(side_lengths[2])

    if(side0 >= side1 and side0 >= side2):
        return side1 * 2 + side2 * 2 + side0 * side1 * side2
    elif(side1 >= side0 and side1 >= side2):
        return side0 * 2 + side2 * 2 + side0 * side1 * side2
    else:
        return side0 * 2 + side1 * 2 + side0 * side1 * side2
    
sum = 0

with open('input.txt') as fp:
    for line in fp:
        thisLength = calculate_ribbon_length(line)
        # print(str(thisLength))
        sum += thisLength

print(str(sum))