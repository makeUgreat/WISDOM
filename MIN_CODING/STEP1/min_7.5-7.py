# atr = map(int,input().split())

lst = [[0 for j in range(2)] for i in range(3)]
numbers = input().split()
    
for i in range(3):
    for j in range(2):
        num = int(numbers[i * 2 + j])
        lst[i][j] = num + 2 
    
for i in lst:
    print(*i)

    
    
# print(atr)