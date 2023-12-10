# return the total value of a single card:
# Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
def checkCard(line):
    outer = line.split(":")
    inner = outer[1].split("|")

    # print("winners:")
    winners = {-1}
    for num in inner[0].split(" "):
        if num != '' and num != " ":
            winners.add(int(num))

    val = 0
    # print("my nums:")
    for num in inner[1].split(" "):
        if num != '' and num != " ":
            if int(num) in winners: 
                if val == 0:
                    val = 1
                else:
                    val *= 2
    
    return val

sum = 0

with open('input.txt') as fp:
    for line in fp:
        # print(line)
        sum += checkCard(line)
        
print(str(sum))