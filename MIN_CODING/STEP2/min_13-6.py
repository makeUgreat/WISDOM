lsts = [
    [4,5,6,1,3,1],
    [2,1,3,6,3,6]
]

n1, n2, n3 = map(int,input().split())

count_n1 = 0
count_n2 = 0
count_n3 = 0

for lst in lsts:
    count_n1 += lst.count(n1)
    count_n2 += lst.count(n2)
    count_n3 += lst.count(n3)

print(f'{n1}={count_n1}개')
print(f'{n2}={count_n2}개')
print(f'{n3}={count_n3}개')