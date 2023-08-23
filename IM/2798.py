import sys
sys.stdin = open('IM/input.txt','r')

N, total = map(int, input().split())
cards = list(map(int, input().split()))

path= [0] * 3
result = -21e8
visit = [False] * N
 
def dfs(level,start,Sum):
    global result 

    if Sum > total:
        return 

    if level == 3:
        # for i in range(3):
        #     print(path[i],end=' ')
        # print()
        if Sum > result:
            result = Sum
        return


    for i in range(start,N):
        if not visit[i]:
            visit[i] = True
            path[level] = cards[i]
            dfs(level+1,i,Sum+cards[i])
            visit[i] = False

dfs(0,0,0)
print(result)