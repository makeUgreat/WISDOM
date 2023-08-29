P = int(input())
N = int(input())

for i in range(1,N+1):
    P *= 2
    P = int(str(P)[::-1])
print(P)