
rules = []
updates = []

def is_valid(update):
    global rules

    for r in rules:
        if update.count(r[0]) > 0 and update.count(r[1]) > 0:
            if update.index(r[0]) > update.index(r[1]):
                return False

    return True

def middle_value(update):
    return int(update[int(len(update) / 2)])

with open('2024/05/input.txt') as fp:    
    for line in fp:
        #print(line.replace('\n', ''))
        if line.find('|') > -1:
            rules.append(line.replace('\n', '').split('|'))
        elif line == '\n':
            pass
        else:
            updates.append(line.replace('\n', '').split(','))

sum = 0

for u in updates:
    if is_valid(u):
        sum += middle_value(u)

print(str(sum))