lsts = [[' ']*3 for _ in range(3)]
def Magic():
    
    index = 1
    for i in range(3):
        for j in range(3):
            
            if i != j:
                if i >= 1 and j <= 1:
                    continue
            lsts[i][j] = index
            index += 1
    
    for lst in lsts:
        print(*lst,sep='')

Magic()