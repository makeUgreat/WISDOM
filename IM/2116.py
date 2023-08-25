import sys
sys.stdin = open('input.txt','r')

import sys
sys.setrecursionlimit(100000)

n = int(input())

dice = []
for i in range(n):
    row = list(map(int,input().split()))
    dice.append(row)

D = ['A','B','C','D','E','F']
against = {
    'A': 'F',
    'F': 'A',
    'B': 'D',
    'D': 'B',
    'C': 'E',
    'E': 'C'
}

max_v = -21e8
def abc(level,bottom_v,Sum):
    global max_v
    ddice = [1,2,3,4,5,6]
    # print(f'현재 까지 최대값 합:{Sum}')

    if level == n:
        max_v =max(max_v,Sum)
        return

    di = dice[level].index(bottom_v) # 주사위 값이 위치한 인덱스
    dp = D[di] # 주사위 값,인덱스가 위치한 주사위상 위치

    top = against.get(dp)
    top_i = D.index(top)
    top_v = dice[level][top_i]

    ddice.remove(bottom_v)
    ddice.remove(top_v)
    print(f'{level}번째 주사위')
    print(f'주사위 아랫면:{bottom_v}')
    print(f'주사위 윗면:{top_v}')
    print(f'남은 주사위:{ddice}')

    abc(level+1,top_v,Sum+max(ddice))


for num in range(6):
    abc(0,dice[0][num],0) # 첫번째 주사위 아랫면 각각 경우의 수

print(max_v)