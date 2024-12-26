
def count_letters(string):
    seen = set()
    for c in string:
        seen.add(c)
    return len(seen)

sum = 0
this_group = ''
with open('2020/06/input.txt') as file:
    for line in file:
        if line == '\n':
            sum += count_letters(this_group)
            this_group = ''
        else:
            this_group += line.strip()
sum += count_letters(this_group)

print(sum)