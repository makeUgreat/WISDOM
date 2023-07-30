position = list(map(int,input().split()))

flag = False
for i in range(len(position)-1):
    
    if abs(position[i] - position[i+1]) > 3:
        flag = True
    
    
if flag:
    print('재배치필요')
else:
    print('완벽한배치')


