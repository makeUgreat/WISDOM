nums = list(map(int,input().split()))

cnt = [0] * (max(nums)+1)

# cnt 배열 등록
for num in nums:
    cnt[num] += 1

# 누적합 등록
for i in range(1,len(cnt)): # 누적합이니까 1번 인덱스부터 시작
    cnt[i] += cnt[i-1]
    # 누적합은 앞으로 만들 sorting 배열의 인덱스가 된다.
# print(cnt)
sorting = [0] * len(nums)

for i in range(len(nums)):
    cnt[nums[i]] -= 1
    index = cnt[nums[i]] #
    sorting[index] = nums[i]   


print(*sorting)
