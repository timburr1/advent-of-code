
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

def reorder(update):
    global rules

    for r in rules:
        if update.count(r[0]) > 0 and update.count(r[1]) > 0:
            i = update.index(r[0])
            j = update.index(r[1])
            if i > j:
                temp = update[i]
                update[i] = update[j]
                update[j] = temp
                return reorder(update)
    return update

with open('2024/05/test.txt') as fp:    
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
    if not is_valid(u):
        sum += middle_value(reorder(u))

print(str(sum))