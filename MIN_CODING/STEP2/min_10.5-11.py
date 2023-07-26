def run(num):
    lsts = []

    if num < 10:
        for i in range(3):
            line = [(1 + (3 * i)) + j for j in range(3)]
            lsts.append(line)
        
        for lst in lsts:
            print(*lst,sep='')
    
    elif num >= 10:
        for i in range(3):
            line = [(3 + (3 * i)) - j for j in range(3)]
            lsts.append(line)
            
        for lst in lsts:
            print(*lst,sep='')                    

        
num = int(input())
run(num)