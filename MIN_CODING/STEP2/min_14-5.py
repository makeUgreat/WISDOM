import sys
sys.stdin = open('MIN_CODING/input.txt','r')

lsts = []
for i in range(3):
    line = list(map(int,input().split()))
    lsts.append(line)
    
sum_count = 0


for i in range(len(lsts)):
    for j in range(len(lsts[i])):
        if i != j:
            if i <= 1:
                if j >= 1:
                    continue
        
        sum_count += lsts[i][j]
        
print(sum_count)
        