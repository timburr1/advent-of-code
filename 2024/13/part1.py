machines = []

def add_machine(args):
    global machines

    new_machine = []
    a = args[0].replace('Button A: X+', '').split(', Y+')
    new_machine.append([int(a[0]), int(a[1])]) # A button specs
    a = args[1].replace('Button B: X+', '').split(', Y+')
    new_machine.append([int(a[0]), int(a[1])]) # B button specs
    a = args[2].replace('Prize: X=', '').split(', Y=')
    new_machine.append([int(a[0]), int(a[1])]) # prize location
    machines.append(new_machine)

def cost(machine):
    min_cost = 0
    a_button = machine[0]
    b_button = machine[1]
    target = machine[2]

    for a in range(101):
        for b in range(101):
            if a * a_button[0] + b * b_button[0] > target[0]:
                break
            elif a * a_button[1] + b * b_button[1] > target[1]:
                break

            if a * a_button[0] + b * b_button[0] == target[0] and a * a_button[1] + b * b_button[1] == target[1]:
                cost = 3 * a + b
                if cost < min_cost or min_cost == 0:
                    min_cost = cost
    return min_cost

with open('2024/13/input.txt') as fp:
    args = []
    for line in fp:
        # print(line.strip())
        if line == '\n':
            add_machine(args)
            args = []
        else:
            args.append(line.strip())
    add_machine(args)
print(str(machines))

total_cost = 0
for m in machines:
    # print(str(m))
    c = cost(m)
    # print(str(c))
    total_cost += c
print(str(total_cost))