cnt = {}
for _ in range(3):
    st = input() 
    
    for s in st:
        cnt[s] = cnt.get(s,0) + 1

flag = 1

for value in cnt.values():
    if value >= 2: 
        flag = 0

if flag: print('Perfect')
else: print('No')
