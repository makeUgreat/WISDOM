a, b, c = map(int,input().split())

for i in range(c):
    for _ in range(a,b+1):
        print(_,end=' ')
        
    print()