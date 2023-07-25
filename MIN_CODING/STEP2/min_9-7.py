import sys
sys.stdin = open("MIN_CODING/input.txt","r")

lsts = [[0]*2 for _ in range(6)]

for i in range(len(lsts)):
    lsts[i] = list(map(int,input().split()))

count = 0
for i in range(len(lsts)):
    if lsts[i][0] < lsts[i][1]:
        tmp = lsts[i][0]
        lsts[i][0] = lsts[i][1]
        lsts[i][1] = tmp
        count += 1



for i in lsts:
    print(*i)
print(f'{count}명')