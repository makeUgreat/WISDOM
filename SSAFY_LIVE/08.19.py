from collections import deque

import sys
sys.stdin = open('input.txt','r')

t = int(input())


for tc in range(1,t+1):
    n = int(input())

    # 맵 만들기
    Map = []
    for _ in range(n):
         row = list(map(int,input().split()))
         Map.append(row)

    # 이전 이동방향에 따라 우회전의 기준이 다름
    # 이전 : 우회전
    # x+1  -> y+1
    # x-1  -> y-1
    # y-1  -> x+1
    # y+1  -> x-1

    q = deque()
    q.append([0,0])
    y = 0
    x = 0
    while q:

        # 사과 위치 저장
        appleline = {}
        for i in range(n):
            for j in range(n):
                if Map[i][j] != 0:
                    appleline[Map[i][j]] = [i,j]



        for key,value in appleline.items():
            if key == 1:
                ay,ax

        # directy = [0,1,0,-1]
        # directx = [1,0,-1,0]
        #
        # dy = y + directy[right_cnt % 4]
        # dx = x + directx[right_cnt % 4]



