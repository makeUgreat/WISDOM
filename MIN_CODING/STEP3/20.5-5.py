st = ord(input()) 

for i in range(st-3,st+4):
    if i > ord('Z'):
        i-=26
    if i < ord('A'):
        i+=26
    print(chr(i),end='')