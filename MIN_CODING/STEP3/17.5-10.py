def masking(mask, target):

    for i in range(len(mask)):
        for j in range(len(mask[i])):
            if mask[i][j] == 1:
                if  3 <= target[i][j] <= 5:
                    return 1
    return 0
           
lsts = [
    [3,1,9],
    [7,2,1],
    [1,0,8]
]
mask = []
masked_list = []

# 마스크 배열을 마스킹 함수를 실행했을 때 
# 바로 만드는게 더 좋아보임 

for _ in range(3):
    line = list(map(int,input().split()))
    mask.append(line)

if masking(mask,lsts):
    print('발견')
else:
    print('미발견')