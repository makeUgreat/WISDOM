lsts = []
for i in range(3):
    line = list(map(int,input().split()))
    lsts.append(line)

target = int(input())

flag = False
for lst in lsts:
    if lst.count(target) >= 1:
        flag = True


if flag: print('존재')

##sssssssss