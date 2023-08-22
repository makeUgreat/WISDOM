import sys
sys.stdin = open('input.txt','r')

colors = ['W','B','R'] # 0,1,2

def dfs(line, color, Sum): # 국기의 줄, 색상, 바꿔야할 칸 합
    global result

    # 바꿔야할 칸이 현재까지의 최소값보다 크다면 탐색이 무의미하므로 백트래킹
    if result <= Sum: return

    if line >= N-1: #마지막 줄까지 탐색하면
        result = Sum  # 합 결과 저장
        return


    for i in range(color, min(3, color+2)): # 조합이니까.. (0,1) (1,2) (2,2)
        temp = 0

        # 다음 탐색이 마지막 줄인데다가 현재 흰색칸이면 블루줄이 없어서 성립할 수 없는 조건이므로 백트래킹
        if line >= N-2 and i == 0: continue

        for j in flag[line]:  # 현재 줄을 순회
            if j != colors[i]: # 줄의 현재 칸이 탐색하고있는 색깔이 아니면
                temp += 1  # 바꿔줘야 하므로 값 하나 올림

        dfs(line+1, i, Sum+temp) # 한줄 더 내려가고 다시 조합 생각


def buildup():
    global result
    for i in flag[0]: # 국기 첫번째 줄 다 흰색
        if i != 'W': result += 1
    for i in flag[-1]: # 국기 마지막 줄
        if i != 'R': result += 1



for t in range(1, int(input())+1):

    N, M = map(int, input().split())
    flag = [list(input()) for _ in range(N)]

    result  = 21e8
    dfs(1,0,0)

    buildup()
    print(f'#{t} {result}')
