
def count_letters(string, num):
    seen = dict()
    for c in string:
        if seen.get(c) == None:
            seen[c] = 1
        else:
            seen[c] += 1

    n = 0
    for i in seen.items():
        if i[1] == num:
            n += 1
    return n

sum = 0
this_group = ''
member_count = 0
with open('2020/06/input.txt') as file:
    for line in file:
        if line == '\n':
            sum += count_letters(this_group, member_count)
            this_group = ''
            member_count = 0
        else:
            this_group += line.strip()
            member_count += 1
sum += count_letters(this_group, member_count)

print(sum)