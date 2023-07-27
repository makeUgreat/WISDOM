lsts = [[0]*5 for _ in range(5)]

row_num, ch1 = input().split()
row_num = int(row_num)
ch1 = ord(ch1)
index = 4

for i in range(len(lsts)):
    for j in range(len(lsts[i])):
        if i == row_num-1:
            lsts[i][j] = chr(ch1 + index)
            index -= 1
                
                

for lst in lsts:
    print(*lst,sep='')


