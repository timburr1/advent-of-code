
mols = set()
rules = dict()

def add_rule(input):
    global rules

    parts = input.split(' => ')
    if rules.get(parts[0]) == None:
        rules[parts[0]] = set()
    rules[parts[0]].add(parts[1])

def react(input, target, step_count):
    global mols, rules

    if input == target:
        return step_count
    return step_count + min_dist

with open('2015/19/test2.txt') as file:
    for line in file:
        if line.count('=>') > 0:
            add_rule(line.replace('\n', ''))
        elif line == '\n':
            continue
        else:
            steps = react('e', line.replace('\n', ''), 0)

print(str(len(steps)))
