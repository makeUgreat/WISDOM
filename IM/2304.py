import sys
sys.stdin = open('IM/input.txt','r')

N = int(input())
arr = [0] * 1001

max_h = -1
max_hL = -21e8

last_L = -21e8
for _ in range(N): 
    L,H = map(int, input().split())
    if H > max_h:
        max_h = H 
        max_hL = L 
    if L > last_L:
        last_L = L 
        
    arr[L] = H 

area = 0
now = 0
height = -21e8

for i in range(max_hL+1): # 가장 높은 기둥까지 
    if arr[i] != 0: # 기둥을 만나고
        if arr[i] > now: # 그 기둥이 지금까지 가장 높았던 기둥보다 더 높으면
            now = arr[i] # 가장 높은 기둥을 교체
    area += now #기둥 면적을 더해간다  

now = 0
for k in range(last_L ,max_hL,-1): # 15,8  가장 뒤 부터 가장 높은 기둥까지
    if arr[k] != 0:
        if arr[k] > now:
            now = arr[k]
    
    area += now
print(area) 