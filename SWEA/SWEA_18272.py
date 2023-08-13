import sys
sys.stdin = open("SWEA/input.txt","r")

T = int(input())
base = ['[',']','{','}','(',')']

for tc in range(1,T+1):
    
    input_st = list(input())
    stack = []
    for chr in input_st: # 정   
        if chr in base:
            stack.append(chr) 
        
        if len(stack) >= 2:
            if stack[-2] == '[' and chr == ']': 
                stack.pop(-1)
                stack.pop(-1)
                continue
            
            if stack[-2] == '{' and chr == '}': 
                stack.pop(-1)
                stack.pop(-1)
                continue
            if stack[-2] == '(' and chr == ')': 
                stack.pop(-1)
                stack.pop(-1)
                continue
    
    if len(stack) == 0:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')