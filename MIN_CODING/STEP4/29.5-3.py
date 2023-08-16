arrs = []
for _ in range(3):
    row = list(map(int,input().split()))
    same = 0

    for i in range(2):
        if row[i] == row[i+1]:
            same = 1

    if same:
        print(row[0]) 
    else:
        print('x')

    

