arr = [
    [3,5,4,2,5],
    [3,3,3,2,1],
    [3,2,6,7,8],
    [9,1,1,3,2]
]


def getSum(y,x):
    Sum = 0

    for i in range( n ):
        for j in range( m ):
            Sum += arr[y+i][x+j]

    return Sum
    
    


n, m = map(int,input().split())

max_v = -21e8
max_i = 0
max_j = 0
for i in range( (4-n)+1 ):
    for j in range( (5-m)+1 ):
        if getSum(i,j) > max_v:
            max_v = getSum(i,j)
            max_i = i
            max_j = j

print(f'({max_i},{max_j})') 