watch = [12,3,6,9]
direct = [0,3,1,2]

num = int(input())

for _ in range(num//90):
    tmp = watch.pop()
    watch.insert(0,tmp)

for i in direct:
    print(watch[i],end=' ')