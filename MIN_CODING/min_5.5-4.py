n1 = int(input())
lst = []

for i in range(n1,n1-5,-1):
    lst.append(i)


def KFC():
    print(*lst,sep='')

KFC()