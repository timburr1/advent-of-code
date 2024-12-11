
letters = 'abcdefghijklmnopqrstuvwxyz'
password = 'hxbxwxba'

def includes_triple(password):
    for i in range(1, len(password)-1):
        a = letters.find(password[i-1])
        b = letters.find(password[i])
        c = letters.find(password[i+1])

        if a == b-1 and b == c-1: 
            # todo: add % operator
            return True
    return False

def includes_two_pairs(password):
    i = 0
    while i < len(password):
        i += 1
        if password[i-1] == password[i]:
            break  
    while i < len(password):
        if password[i-1] == password[i]:
            return True
    return False

def is_valid(password):
    if password.count('i') > 0 or password.count('o') > 0 or password.count('l') > 0:
        return False
    if not includes_triple(password):
        return False
    return includes_two_pairs(password)

def increment(password):
    for i in range(len(password)-1, -1, -1):
        continue
    return password

while not is_valid(password):
    password = increment(password)