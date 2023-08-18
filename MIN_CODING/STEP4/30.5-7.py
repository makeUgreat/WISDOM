# 최대레벨 5
# 브랜치 5 
# 해당 레벨에서 합이 10~20 사이면 리턴하고 카운트

nums = list(map(int,input().split()))

visit = [False] * 5
cnt = 0

def abc(level,start,Sum):
    global cnt
    
    if 10 <= Sum <= 20:
        cnt += 1
    
    if Sum > 20:
        return

    if level == len(nums):
        return 
    
    for i in range(start,5):
        abc(level+1, i+1, nums[i] + Sum )


abc(0,0,0)

print(cnt)