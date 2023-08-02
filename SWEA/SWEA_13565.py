import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1,T+1):
    fuel, destination, num_powered_stop = map(int,input().split())
    powered_stops = list(map(int,input().split()))

    bus = 0  #버스의 현재 위치
    road = (list(i for i in range(destination+1)))
    flag = 1
    cnt = 0 # 충전횟수
    init_fuel = fuel # 충전량 할당
    for i in range(len(road)): # 버스가 road 이동
        if bus == destination:
            break

        if flag:
            for power in powered_stops:
                if road[i] == power: # 현재 길에 충전소가 있으면
                    if fuel == 0:
                        fuel = init_fuel
                        cnt += 1
                        flag = 0
                        break
                    if road[i + fuel] in powered_stops:  # 남은 연료만큼 갔을 때 파워가 있는지 확인
                        flag = 0 # 있으면.. 충전안하고 패스
                        break

                    else: # 없으면
                        fuel = init_fuel # 할당 충전량만큼 충전
                        cnt += 1 # 충전횟수 카운트
                        flag = 0
                        break
            fuel -= 1 # 한칸 이동했으니 연료깎음
            flag = 1






    print(f'#{tc} {cnt}')