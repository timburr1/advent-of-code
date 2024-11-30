
CARD_VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

def sort(hand_str):
    return ""

with open('input.txt', 'r') as file:
    lines = file.read().splitlines()

hands = []
for line in lines:
    data = line.split(" ")
    hand = sort(data[0])
    bid = int(data[1])
    hands.append((hand, bid))

for hand in hands:
    print(hand)