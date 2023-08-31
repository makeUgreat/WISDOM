N = int(input())

bombs = list(map(int,input().split()))

stack = []
for bomb in bombs:
    if len(stack) >= 2 and stack[-1] == bomb and stack[-2] == bomb:
        # while stack -> 스택이 비지 않았고, stack 의 마지막이 bomb이면.. # 즉 연속된게 나오면 남은게 있는 한 계속 팝
        while stack and stack[-1] == bomb:
            stack.pop()
    else:
        stack.append(bomb)

ans = sorted(stack,key=lambda x: x)
print(*ans)