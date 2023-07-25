lst_1 = [3,5,2,4,1]
lst_2 = [[9,8], [7,1], [3,4]]

x = int(input())

if x % 2 == 0:
    for i in lst_2:
        for k in i:
            print(k,end='')
        print()
else:
    for j in lst_1:
        print(j,end='')