import sys
sys.stdin = open('SWEA/input.txt','r')

        
T = int(input())

for i in range(1,T+1):
    min_v = 1000000
    max_v = 1 
    N = int(input())
    arr = list(map(int,input().split()))
    
    for j in range(N):
        if arr[j] < min_v:
            min_v = arr[j]
        
        if arr[j] > max_v:
            max_v = arr[j]
        
    print(f'#{i} {max_v-min_v}')
        
        
