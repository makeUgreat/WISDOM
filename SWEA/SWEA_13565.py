import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1,T+1):

    fuel, destination, power_station = map(int,input().split())
    num_power_station = list(map(int,input().split()))
    need_charge = 0
    flag = 1
    for i in range(power_station):
        if num_power_station[i] - num_power_station[i-1] > fuel:
            flag = 0
            break

    if flag:
        if (destination+1) % fuel == 0:
            need_charge = ((destination + 1) // fuel) - 1
        else:
            need_charge = (destination+1) // fuel



    print(f'#{tc} {need_charge}')











