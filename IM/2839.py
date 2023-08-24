N = int(input())
bag = [3,5]
flag = 1
min_level = 21e8
visit = [[False]*5000 for _ in range(5000)]
def comb(level,bag3,bag5):
    global flag, min_level
    # visit[bag3,bag5] = True

    Sum = (3*bag3)+(5*bag5)

    if level > 5000:
        return

    if Sum > N:
        return

    if Sum == N:
        flag = 0
        if level < min_level:
            min_level = level
        return

    if visit[bag3][bag5]:
        return
    visit[bag3][bag5] = True

    for i in range(2):
        if bag[i] == 3:
            comb(level+1,bag3+1,bag5)
        if bag[1] == 5:
            comb(level+1,bag3,bag5+1)



comb(0,0,0)
if flag:
    print(-1)
else:
    print(min_level)