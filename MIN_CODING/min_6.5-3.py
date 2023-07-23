value = map(int,input().split())
lst = []
lst2 = []


for i in value:
    lst.append(i)

lst2 = lst.copy()
print(*lst)
print(*lst2)
