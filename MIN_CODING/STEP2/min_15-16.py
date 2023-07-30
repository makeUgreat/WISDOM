ch1 = ord(input())


lsts = [] 

j = 0 # 문자 통제
k = 0 # 열 통제
while j <= 4:
    i = 3 - k 
    line = []
    
    while i < (6 - (3*j)):   # 6, 3, 0

        line.append(chr(ch1 + i)) 
        i += 1 
        
    j += 1
    k += 2    
    lsts.append(line)

for lst in lsts: 
    print(*lst,sep='')