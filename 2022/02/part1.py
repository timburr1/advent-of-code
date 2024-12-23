
total_score = 0

# Rock     = A = X
# Paper    = B = Y
# Scissors = C = Z
def score(input):
    line_score = 0
    vals = input.replace('\n', '').split(' ')
    if vals[1] == 'X':
        line_score += 1

        if vals[0] == 'A':
            line_score += 3
        elif vals[0] == 'C':
            line_score += 6

    if vals[1] == 'Y':
        line_score += 2
        
        if vals[0] == 'B':
            line_score += 3
        elif vals[0] == 'A':
            line_score += 6

    if vals[1] == 'Z':
        line_score += 3
        
        if vals[0] == 'C':
            line_score += 3
        elif vals[0] == 'B':
            line_score += 6

    return line_score

with open('2022/02/input.txt') as fp:
    for line in fp:
        total_score += score(line)

print(total_score)
