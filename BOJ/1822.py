import sys
sys.stdin = open('input.txt','r')

nA, nB = map(int,input().split())
nums_A = list(map(int,input().split()))
nums_B = list(map(int,input().split()))

def BS(target, arr):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        mid_v = arr[mid]

        if target == mid_v:
            return True

        if target < mid_v:
            end = mid - 1

        elif target > mid_v:
            start = mid + 1

    return False

nums_A.sort()
nums_B.sort()
ans = []

for num in nums_A:
    if not BS(num, nums_B):
        ans.append(num)

print(len(ans))
print(*ans)