import sys
sys.stdin = open('IM/input.txt','r')


short = []
for _ in range(9):
    short.append(int(input()))
short.sort()

path = [0]*7
visit = [False] * 9
flag = 0
def com(level,start,Sum):
    global flag
    
    if flag: return

    if Sum > 100:
        return
    
    if level == 7:
        if Sum == 100:
            flag = 1 
            for i in range(7):
                print(path[i])
            return
        else:
            return 

    for i in range(9):
        if not visit[i]:
            visit[i] = True
            path[level] = short[i]
            com(level+1,i,Sum+short[i])
            visit[i] = False
com(0,0,0)