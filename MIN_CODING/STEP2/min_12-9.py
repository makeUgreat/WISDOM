def print_func(lsts):
    
    for lst in lsts:
        for ls in lst:
            if ls == 0:
                print(' ',end='')
                continue
            print(ls,end='')
        print()    


ch1 = input()
lsts = [[0]*3 for _ in range(3)]

if '0' <= ch1 <= '9':
    value = 6
    for i in range(len(lsts)):
        for j in range(len(lsts[i])):

            if not i == j:
                if i >= 1 and j <= 1:
                    continue
            lsts[i][j] = value
            value -= 1
    print_func(lsts)

if ch1.isupper():
    value = 1
    for i in range(len(lsts)-1,-1,-1): # 2,1,0
        for j in range(len(lsts[i])): # 0,1,2 

            if not i == j:
                if j >= 1 and i <= 1:
                    continue
            lsts[i][j] = value
            value += 1
    print_func(lsts)



