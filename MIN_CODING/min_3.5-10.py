x = int(input())

data = [(i*2)-1 for i in range(1,x+1)]

for i in data:
    print(int(i), end=' ')    
    
    
    
#GPT 코드
x = int(input())

for i in range(1, x+1):
    print((i*2) - 1, end=' ')