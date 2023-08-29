arr = [ list(input()) for _ in range(5)]

rotate = list(zip(*arr))

rotate[1],rotate[3] = rotate[3],rotate[1]
rotate2 = list(zip(*rotate))

target = ['M','A','P','O','M']

flag = 0
for i in range(5):
    cnt = 0
    for j in range(5):
        if rotate2[i][j] == target[j]:
            cnt += 1
        else:
            cnt = 0

        if cnt == 5:
            flag = 1


if flag: print('yes')
else: print('no')