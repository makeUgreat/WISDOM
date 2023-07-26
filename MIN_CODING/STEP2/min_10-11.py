import sys
sys.stdin = open('MIN_CODING/input.txt','r')

lsts = [] 
for i in range(4):
    line = list(map(int,input().split()))
    lsts.append(line)

for i in range( len(lsts) ):
    for j in range( len(lsts[i]) ):

        if lsts[i][j] == 0:
            lsts[i][j] = '!'

        elif lsts[i][j] % 2 == 0:
            lsts[i][j] = '#'
        
        elif lsts[i][j] % 2 == 1:
            lsts[i][j] = '@' 
        
        

for lst in lsts:
    print(*lst,sep='',end='')
    print()
