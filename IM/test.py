n,m=map(int,input().split())
lst=[list(input().split()) for _ in range(m)]
group=[0]*200
lst.sort(key=lambda x:int(x[2]))

def findboss(a):
    if not group[ord(a)]:
        return a
    ret = findboss(group[ord(a)])
    group[ord(a)] = ret
    return ret

def union(x,y,i):
    global group,total,cnt
    x_boss,y_boss=findboss(x),findboss(y)
    if x_boss==y_boss:
        return
    cnt+=1
    total+=int(lst[i][2])
    group[ord(y_boss)]=x_boss

total=0  # 총 공사비용
cnt=0   # 연결시킨 선의 개수

for i in range(m):
    if cnt==n-1:
        print(total)
        break
    union(lst[i][0],lst[i][1],i)
