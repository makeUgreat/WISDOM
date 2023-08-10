st = input()

target = 'GHOST'
found = False

for i in range(len(st) - len(target) + 1):
    if st[i: i+len(target)] == target:
        found = True
        break
    
if found:
     print('존재')
else:
    print('존재하지 않음')