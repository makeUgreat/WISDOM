import sys
sys.stdin = open("WISDOM/BAEKJOON/input.txt","r")

N,M = map(int,input().split()) # 2, 3
lsts = []  # N*M 배열

for i in range(N):
    line = list(map(int,input().split())) # 1 2 4 # 8 16 32
    lsts.append(line)

sum_cases = int(input())

for case in range(sum_cases):
    i,j,x,y = map(int,input().split())
    
    sum_ = 0    
    for row in range(i-1,x):
        for col in range(j-1,y): 
            sum_ += lsts[row][col]

    print(sum_)