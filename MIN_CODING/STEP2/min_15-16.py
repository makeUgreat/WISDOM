ch1 = ord(input())-1

lsts = [] 

j = 2 
k = 0 
i = 4
while i >= 1:
    line = []
    k = i
    while i <= k+j:
        line.append(chr(ch1 + i))
        i += 1 
    j -= 1
    i = int(i / 2)-1 
    lsts.append(line)

for lst in lsts: 
    print(*lst,sep='')