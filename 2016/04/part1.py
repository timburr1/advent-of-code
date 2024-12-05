
import hashlib

door_id = 'reyedfim'
# door_id = 'abc'
password = ''
i = 0

def hash(i):
    global door_id

    my_string = door_id + str(i)
    return hashlib.md5(my_string.encode('utf-8')).hexdigest()

while len(password) < 8:
    h = hash(i)
    #print(i)
    if h.startswith('00000'):
        password += h[5]
    i += 1

print(password)