Branch,Level = map(int,input().split())

cnt = 0
def abc(level):
    global cnt
    cnt += 1

    if level == Level:
        return
    

    for i in range(Branch):
        abc(level+1)

abc(0)

print(cnt)