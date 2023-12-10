
CARD_VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

with open('input.txt') as fp:
    for line in fp:
        parse(line.strip())