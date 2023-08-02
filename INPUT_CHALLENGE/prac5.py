lst = [
    [1,5,4,2],
    [1,3,4,2],
    [3,5,3,2],
    [2,6,4,1]
]

def isPattern(y,x):
    sum_ = 0
    max_v = -21e8
    for i in range(2):

        for j in range(3):
            sum_ += lst[i][j]
            if max_v < sum_:
                max_v = sum_

    return max_v

# 2*3배열
for i in range(4):
    for j in range(4):
        ret = isPattern(i,j)

print(ret)


####
Max = -21e8
def getsum(a,b):
    sum_ = 0
    for i in range(2):
        for j in range(3):
            sum_ += lst[a+i][b+j]

    return sum_

for i in range(3):
    for j in range(2):
        ret = getsum(i,j)
        if ret>Max:
            Max=ret

print(Max)




