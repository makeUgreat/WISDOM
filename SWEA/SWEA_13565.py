import sys
sys.stdin = open("SWEA/input.txt", "r")

T = int(input())

for tc in range(1,T+1):

    K,N,M = map(int,input().split())
    # K = 한번에 갈 수 있는 거리
    # N = 종점번호(배열은 0 포함하여 +1만큼 생성)
    # M = 충전기 설치된 정류장 개수

    # 정류장 배열 생성
    stops = [ i for i in range(N+1) ]
    # 충전소 배열 생성
    power = list(map(int,input().split()))

    i = 0 # 현재 버스 위치
    charge  = 0 # 충전횟수
    find_charge = 0
    flag = 1 
    while flag:
        
        find_charge = 0

        for j in range(K,0,-1):

            if i+j >= N:
                find_charge = 1
                flag = 0
                break 

            if i+j < N:
                if stops[i+j] in power:
                    i = i+j
                    find_charge = 1
                    charge += 1
                    break

        if find_charge == 0:  # 갈 수 있는 거리에 충전소가 없으면 다 멈추고 0 출력
            charge = 0
            flag = 0
            break


    print(f'#{tc} {charge}')
        
       










