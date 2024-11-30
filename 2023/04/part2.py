
cards = {}
card_count = {}

def scratch_card(card_num, card_str, repeat):
    # print(str(repeat) + " x " + str(card_num))
    inner = card_str.split("|")
    
    # print("winners:")
    winners = {-1}
    for num in inner[0].split(" "):
        if num != '' and num != " ":
            # print(num)
            winners.add(int(num))

    val = 0
    # print("my nums:")
    for num in inner[1].split(" "):
        if num != '' and num != " ":
            # print(num)
            if int(num) in winners: 
                val += 1
    # print("won: " + str(val))

    for i in range(1, val + 1):
        card_count[card_num + i] += repeat
    # print(card_count)
    
# return the total value of a single card:
# Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
def parse_line(line):
    outer = line.split(":")
    card_num = int(outer[0].replace("Card ", ""))
    cards[card_num] = outer[1]
    card_count[card_num] = 1

with open('input.txt') as fp:
    for line in fp:
        # print(line)
        parse_line(line)

# print( card_count)

for card_num in cards:
    scratch_card(card_num, cards[card_num], card_count[card_num])

#print( card_count)

sum = 0

for i in card_count:
    sum += card_count[i]

print(str(sum))