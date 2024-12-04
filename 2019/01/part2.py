
def required_fuel(mass):
    fuel = int(mass / 3) - 2
    
    print(str(fuel))
    
    if fuel <= 0:
        return 0
    
    return fuel + required_fuel(fuel)

total_fuel = 0

with open('2019/01/input.txt') as fp:
    for line in fp:
        rf = required_fuel(int(line.replace('\n', '')))
        print(str(rf))
        total_fuel += rf

print (str(total_fuel))
