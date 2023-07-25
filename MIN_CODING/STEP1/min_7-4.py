lst = list(map(int,input().split()))
sum2 = 0

for i in range(3,8):
    sum2 += lst.count(i)
    
print(sum2)


