def CountLine(lsts):
    
    for lst in lsts:
        name = ''.join(lst)
        print(f'{len(lst)}={name}')
        
    
    
    
lsts = [] 
for i in range(3):
    line = list(input())
    lsts.append(line)
    
CountLine(lsts)