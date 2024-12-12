
letters = 'abcdefghijklmnopqrstuvwxyz'
password = 'hxbxxzaa'

def includes_triple(password):
    for i in range(1, len(password)-1):
        a = letters.find(password[i-1])
        b = letters.find(password[i])
        c = letters.find(password[i+1])

        if a == b-1 and b == c-1: 
            return True
    return False

def includes_two_pairs(password):
    i = 0
    while i < len(password)-1:
        i += 1
        if password[i-1] == password[i]:
            i += 2
            break  
    while i < len(password):
        if password[i-1] == password[i]:
            return True
        i += 1
    return False

def is_valid(password):
    if password.count('i') > 0 or password.count('o') > 0 or password.count('l') > 0:
        return False
    if not includes_triple(password):
        return False
    return includes_two_pairs(password)

def increment(password):
    for i in range(len(password)-1, -1, -1):
        idx = letters.find(password[i])
        if idx == 25: #z, need to carry
            password = password[:i] + 'a' + password[i+1:]
        elif idx == 7 or idx == 10 or idx == 13: # i, l, o
            password = password[:i] + letters[idx+2] + password[i+1:]
            break
        else:
            password = password[:i] + letters[idx+1] + password[i+1:]
            break
    return password

# print(is_valid('hijklmmn'))
# print(is_valid('abbceffg'))
# print(is_valid('abbcegjk'))

# print(is_valid('hxbxwxba'))
# print(is_valid('aabbdef'))

while not is_valid(password):  
    print(password)  
    password = increment(password)

print('\n\n--------------------\n\n')
print(password)