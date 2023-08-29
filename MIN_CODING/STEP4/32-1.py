N = int(input())
arr = []
for _ in range(N):
    name,score = input().split()
    arr.append([name,int(score)])
    ans = sorted(arr,key=lambda x: -x[1])

    for i in range(len(ans)):
        if i > 2: continue
        print(ans[i][0],end=' ')
    print()




