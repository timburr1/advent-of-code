
diagnostic_report = []

def most_common_value(diagnostics, index):
    zeroes = 0
    ones = 0

    for d in diagnostics:
        if d[index] == '0':
            zeroes += 1
        else:
            ones += 1

    if zeroes > ones:
        return '0'
    return '1'

def oxygen_rating(diagnostics, index):
    if len(diagnostics) == 1:
        return diagnostics[0]

    v = most_common_value(diagnostics, index)
    valid_diagnostics = []
    for d in diagnostics:
        if d[index] == v:
            valid_diagnostics.append(d)
    return oxygen_rating(valid_diagnostics, index+1)

def least_common_value(diagnostics, index):
    zeroes = 0
    ones = 0

    for d in diagnostics:
        if d[index] == '0':
            zeroes += 1
        else:
            ones += 1

    if zeroes > ones:
        return '1'
    return '0'

def co2_rating(diagnostics, index):
    if len(diagnostics) == 1:
        return diagnostics[0]
    
    v = least_common_value(diagnostics, index)
    valid_diagnostics = []
    for d in diagnostics:
        if d[index] == v:
            valid_diagnostics.append(d)
    return co2_rating(valid_diagnostics, index+1)

with open('2021/03/input.txt') as fp:
    for line in fp:
        diagnostic_report.append(line.replace('\n', ''))

print(oxygen_rating(diagnostic_report, 0))
# 010110110011
print(co2_rating(diagnostic_report, 0))
# 110001101010

# 1459 * 3178 = 4,636,702
