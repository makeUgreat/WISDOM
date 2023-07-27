n = int(input())
arr= []
for i in range(3) :
    a = []
    for j in range(4) :
        if i+j >=2 :
            a.append(n)
            n += 1
        else : 
            a.append(' ')
    arr.append(a)
for a in arr :
    print(*a, sep='')



