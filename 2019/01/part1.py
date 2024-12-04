
def required_fuel(mass):
    # print(str(int(int(mass) / 3) - 2))
    return int(int(mass) / 3) - 2

total_fuel = 0

with open('2019/01/input.txt') as fp:
    for line in fp:
        total_fuel += required_fuel(line.replace('\n', ''))

print (str(total_fuel))
