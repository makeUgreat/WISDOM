N = int(input())
info = [ list(map(int,input().split())) for _ in range(N)]
K = int(input())
K_power = (list(map(int,input().split())))

# 체력을 요소별로 나눠 다시 저장
for i in range(N):
    health = info[i][2]

    digit = [int(digit) for digit in str(health)]
    info[i][2] = digit


# 요소별로 나뉜 체력을 뒤에서부터 바람세기 범위만큼 하나씩 빼줌
# 연산을 마친 후 0이 된 요소는 빼줌

cnt = 0
for cloud in K_power: # 4,2
    for i in range(N):
        # print(f'{cloud}세기 바람 분 결과:{info}')
        for k in range(len(info[i][2])-1,-1,-1):

            info[i][2][k] -= cloud

            if info[i][2][k] <= 0:
                info[i][2].pop(k)
                break
            break

for i in range(N):
    cnt += len(info[i][2])

print(cnt)