lst1 = [
    [0,0,1,0,0],
    [0,0,1,1,1]
]

lst2 = [
    [3,5,4,1,1],
    [3,5,2,5,6]
]

flag = 0
num = int(input())
for i in range(len(lst1)):
    for j in range(len(lst1[i])):
        
        if lst1[i][j] == 1:
            if lst2[i][j] == num:
                flag = 1
    
if flag:
    print(f'{num} 존재')
else:
    print(f'{num} 없음')