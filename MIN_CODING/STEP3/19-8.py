import sys
sys.stdin = open("MIN_CODING/STEP3/input.txt","r")

def rectSum(y,x):  # 2*3 크기만큼 합 
    Sum = 0
    for i in range(2):
        for j in range(3):
            Sum += lsts[i+y][j+x]
        
    return Sum 

lsts = []
for _ in range(4):
    line = list(map(int,input().split()))
    lsts.append(line)


max_sum = -21e8
max_i = 0
max_j = 0
for i in range(3):
    for j in range(2):
        if rectSum(i,j) > max_sum:
            max_sum = rectSum(i,j)
            max_i = i
            max_j = j

print(f'({max_i},{max_j})')
    