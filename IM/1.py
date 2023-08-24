N = int(input())
bag = [3, 5]
flag = False
min_level = 21e8
visit = [False] * 5000

def comb(level, bag3, bag5):
    global flag, min_level

    if level == 5000:
        return

    if bag3 * 3 + bag5 * 5 > N:
        return

    if bag3 * 3 + bag5 * 5 == N:
        flag = True
        if bag3 + bag5 < min_level:
            min_level = bag3 + bag5
        return

    if visit[bag3 * 3 + bag5 * 5]:
        return
    visit[bag3 * 3 + bag5 * 5] = True

    comb(level + 1, bag3 + 1, bag5)
    comb(level + 1, bag3, bag5 + 1)

comb(0, 0, 0)

if flag:
    print(min_level)
else:
    print(-1)
