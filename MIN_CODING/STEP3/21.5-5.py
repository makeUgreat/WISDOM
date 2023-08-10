nums = list(map(int,input().split()))

cnt = [0] * (max(nums)+1)

for num in nums:
    cnt[num] += 1

for i in range(len(cnt)):
    cnt[i] += cnt[i-1]


sorting = [0] * len(nums)

for i in range(len(nums)):
    cnt[i] -= 1
    sorting[cnt[i]] = cnt[i]   


print(sorting)
