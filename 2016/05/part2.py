
import hashlib

door_id = 'reyedfim'
# door_id = 'abc'
password = ['', '', '', '', '', '', '', '']
i = 0
c = 0

def hash(i):
    global door_id

    my_string = door_id + str(i)
    return hashlib.md5(my_string.encode('utf-8')).hexdigest()

while c < 8:
    h = hash(i)
    # print(i)
    if h.startswith('00000') and ['0', '1', '2', '3', '4', '5', '6', '7'].count(h[5]) == 1 and password[int(h[5])] == '':
        print(h)
        password[int(h[5])] = h[6]
        c += 1
    i += 1

print(password)