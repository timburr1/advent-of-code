
seen = set()

def get_row(input):
    # print(input)

    # B = 1, F = 0
    r = 0
    for i in range(len(input)):
        if input[i] == 'B':
            r +=  2 ** (6-i)
    return r

def get_seat(input):
    # print(input)

    # R = 1, L = 0
    r = 0
    if input[0] == 'R':
        r += 4
    if input[1] == 'R':
        r += 2
    if input[2] == 'R':
        r += 1
    return r

with open('2020/05/input.txt') as file:
    for line in file:
        # print(line.strip())
        row = get_row(line[:7])
        seat = get_seat(line[7:10])
        seat_id = row * 8 + seat
        seen.add(seat_id)

for i in range(min(seen), max(seen)):
    if not {i} <= seen:
        print(i)
        break
