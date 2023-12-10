

def get_coordinates_to_check(full_text):
    lines = full_text.splitlines()
    coordinates = {}

    # TODO https://github.com/SlowFlo/advent_of_code_2023/blob/main/Day%203%20-%20Gear%20Ratios/part%202/gear_ratios.py

    return coordinates

def sum_gear_ratios(full_text):
    coordinates_to_check = get_coordinates_to_check(full_text)
    lines = full_text.splitlines()

    sum = 0

    for i in range(0, len(line)):
        if line[i] == '*':
            sum += checkGearRatio(i, lineNum)

    return sum

with open('input.txt') as fp:
    input_text = fp.read()

    print(str(sum_gear_ratios))
    