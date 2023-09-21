import sys
sys.stdin = open('input.txt','r')

N = int(input())
have = list(map(int,input().split()))
M = int(input())
need = list(map(int,input().split()))


def bs(target,have):
    start = 0
    end = len(have)-1

    while start <= end:
        mid = (start+end)//2
        mid_v = have[mid]

        if target == mid_v:
            return 'yes'

        if target < mid_v: # 타겟이 미드인덱스의 값보다 작으면
            end = mid - 1  # 미드보다 큰 값들은 확인할 필요가 없다

        elif target > mid_v: # 타겟이 미드인덱스의 값보다 크면
            start = mid + 1  # 미드보다 작은 값들은 확인할 필요가 없다


    return 'no'

have.sort()
for one in need:
    print(bs(one,have),end=' ')