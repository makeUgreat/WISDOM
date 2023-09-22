import sys
sys.stdin = open('input.txt','r')

n,m = map(int,input().split())
nums = list(map(int,input().split()))
dp = [0] * (n+1)

for _ in range(m):
    i,j = map(int,input().split())
    dp[i+1] = nums[i] + nums[i]

    part_sum = dp[j] - dp[i - 1]
    print(dp[j])