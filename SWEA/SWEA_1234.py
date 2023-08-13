import sys
sys.stdin = open("SWEA/input.txt","r")

for tc in range(1,11):
    
    
    str_len, st = input().split()
    stack = []
    str_len = int(str_len)
        
    for i in range(str_len):
        if not stack or stack[-1] != st[i]:
            stack.append(st[i])
        else:
            stack.pop()
    
    
    print(f'#{tc}',end=' ')
    print(*stack,sep='')
    