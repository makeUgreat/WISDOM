import sys
sys.stdin = open('input.txt','r')

N = int(input())
check_list = list(map(int,input().split()))
M = int(input())
have_list = list(map(int,input().split()))


def BS(target,arr):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start+end) // 2
        mid_v = arr[mid]

        if target == mid_v:
            return 1

        if target < mid_v:
            end = mid - 1

        elif target > mid_v:
            start = mid + 1

    return 0



sorted_check = sorted(check_list)
for num in have_list:
    print(BS(num,sorted_check))

