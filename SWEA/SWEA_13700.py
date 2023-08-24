import sys
sys.stdin = open('SWEA/input.txt','r')


T = int(input())


for tc in range(1,T+1):
    
    def bsSearch(end,target):
        start = 1
        cnt = 0
        
        while start <= end:
            mid = (start+end)//2 
            cnt += 1
            
            if mid == target:
                return cnt

            if target < mid: # 찾으려는 값이 중간값보다 작다면
                end = mid # 다시 찾으려는 구간의 마지막을 mid-1로 설정 
            
            if target > mid: # 찾으려는 값이 중간값보다 크다면
                start = mid # 다시 찾으려는 구간의 처음을 mid+1로 설정    
        
        return -1
                        
    
    P,Pa,Pb = map(int,input().split())
    
    
    if bsSearch(P,Pa) > bsSearch(P,Pb):
        ans = 'B'
    if bsSearch(P,Pa) < bsSearch(P,Pb):
        ans = 'A'
    if bsSearch(P,Pa) == bsSearch(P,Pb):
        ans = 0

    
    print(f'#{tc} {ans}')