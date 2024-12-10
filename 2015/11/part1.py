
password = 'hxbxwxba'

def is_valid(password):
    if password.count('i') > 0 or password.count('o') > 0 or password.count('l') > 0:
        return False

def increment(password):
    return password

while not is_valid(password):
    password = increment(password)