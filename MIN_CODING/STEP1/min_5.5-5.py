arr = [4, 1, 2, 3, 5]

x = input()

if x == 'a' or x == 'b' or x == 'c':
    for i in range(3,-1,-1):
        print(arr[i],end=' ')
else: 
    for j in range(4,0,-1):
        print(arr[j],end=' ')