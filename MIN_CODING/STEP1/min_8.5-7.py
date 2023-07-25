lst = [[0]*3 for i in range(3)]
y, x, a = map(int,input().split())

lst[y][x] = a

for i in lst:
    print(*i)