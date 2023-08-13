import sys
sys.stdin = open("SWEA/input.txt","r")

T = int(input())

for tc in range(1,T+1):
    
    st = input() 
    
    stack = [] 
    for i in range(len(st)):
        if not stack or stack[-1] != st[i]:
            stack.append(st[i])
        else:
            stack.pop()
        
        
    print(f'#{tc} {len(stack)}')
    