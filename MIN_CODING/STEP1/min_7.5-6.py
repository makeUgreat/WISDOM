lst = [[0 for i in range(4)] for j in range(2)]


x,y = map(int,input().split())

lst[x][y] = 1

for i in lst:
    print(*i)