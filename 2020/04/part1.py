
def is_valid(passport):
    # print(passport)
    is_valid = passport.count('byr:') == 1 and passport.count('iyr:') == 1 and passport.count('eyr:') == 1 and passport.count('hgt:') == 1 and passport.count('hcl:') == 1 and passport.count('ecl:') == 1 and passport.count('pid:') == 1
    # print(str(is_valid))
    return is_valid

valid_passprt_count = 0

with open('2020/04/input.txt') as file:
    this_passport = ''
    for line in file:
        if line == '\n':
            if is_valid(this_passport):
                valid_passprt_count += 1
            this_passport = ''
        else:
            this_passport += line
    if is_valid(this_passport):
        valid_passprt_count += 1

# print('\n----------\n')
print(str(valid_passprt_count))