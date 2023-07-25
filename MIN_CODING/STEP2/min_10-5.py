
num = int(input())
lsts = []

if num % 5 == 1:
    for i in range(9,6,-1):
        line = [i-(3*k) for k in range(3)]
        lsts.append(line)

if num % 5 == 2:
    for i in range(7,0,-3):
        line = [i+(1*k) for k in range(3)]
        lsts.append(line)
    
else:
    for i in range(10,13):
        line = [i+(3*k) for k in range(3)]
        lsts.append(line)    

for lst in lsts:
    print(*lst)
    