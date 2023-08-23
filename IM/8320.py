n = int(input())


# 기본적으로 정사각형 갯수가 조합가능한 갯수
# + 두 수를 곱했을 때 짝수면 직사각형
# - 두 수가 같으면 정사각형형
# 제곱수는 정사각형

square = []
for i in range(1,n+1):
    square.append(i)

path = [0] * 2
cnt = 0
g_cnt = 0
visit = [False] * len(square)
def com(level,start):
    global cnt
    global g_cnt
    if level == 2:
        # for i in range(2):
        #     print(path[i],end=' ')
        # print()
        if path[0]*path[1] <= n:
            if path[0] == path[1]:
                g_cnt += 1
                print(f'{path[0]}*{path[1]} -> ',end=' ')
                print(f'정사각형:{g_cnt}')
                return
            else:
                print(f'{path[0]}*{path[1]}')
                cnt += 1
                print(f'직사각형:{cnt}')
                return
        return


    for i in range(start,len(square)):
            path[level] = square[i]
            com(level+1,i)

com(0,0)
print(g_cnt+cnt)