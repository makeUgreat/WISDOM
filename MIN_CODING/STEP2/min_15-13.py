lsts = [
    ['D','A','T','A','W'],
    ['B','B','Q','K']
]

n1 = int(input())

if n1 % 2 != 0:
    lsts[0].sort()
elif n1 % 2 == 0:
    lsts[1].sort()


for lst in lsts:
    print(*lst,sep='')