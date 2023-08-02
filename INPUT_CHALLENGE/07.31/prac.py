
lst = [4,3,5,1,7,5,6,8,1,6,9,5]
target = list(map(int,input().split()))
n = int(input())
max_ = -21e8
answer = 0

# sum_ = 0
# for index in target:
#     sum_ = 0
#     for i in range(n):덱
#         sum_ += lst[index+i]
#     print(f'{index}번 인스로 부터 연속된 n개({n}개)의 합은 {sum_} 이고')

def getsum(t):
    sum = 0
    for i in range(t,t+n):
        sum += lst[i]
    return sum


for i in range(len(target)):
    ret = getsum(target[i])
    if ret > max_:
        max_ = ret
        answer = target[i]

print(answer,max_)