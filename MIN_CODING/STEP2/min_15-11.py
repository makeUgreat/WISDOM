lsts = []

for _ in range(4):
    line = list(input())
    lsts.append(line)
    
flag1 = False
flag2 = False
for lst in lsts:
    if 'A' in lst and 'B' in lst:
        flag1 = True
    elif 'A' in lst or 'B' in lst:
        flag2 = True

        
if flag1:
    print('대발견')
elif flag2:
    print('중발견')
else:
    print('미발견')