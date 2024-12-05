
diagnostic_report = []

def gamma():
    result = ''

    for x in range(0, len(diagnostic_report[0])):
        zero_count = 0
        ones_count = 0

        for y in range(0, len(diagnostic_report)):
            if diagnostic_report[y][x] == '0':
                zero_count += 1
            else:
                ones_count += 1

        if zero_count > ones_count:
            result += '0'
        else:
            result += '1'

    return result

def epsilon():
    result = ''

    for x in range(0, len(diagnostic_report[0])):
        zero_count = 0
        ones_count = 0

        for y in range(0, len(diagnostic_report)):
            if diagnostic_report[y][x] == '0':
                zero_count += 1
            else:
                ones_count += 1

        if zero_count < ones_count:
            result += '0'
        else:
            result += '1'

    return result

with open('2021/03/input.txt') as fp:
    for line in fp:
        diagnostic_report.append(line.replace('\n', ''))

print(gamma())
print(epsilon())

# 000011011010
# 111100100101

# 218 * 3877 = 845,186
