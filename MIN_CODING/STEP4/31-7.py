n = int(input())

arr = []
for _ in range(n):
    st = input()
    arr.append([len(st),st])

arr.sort()

for a in arr:
    print(a[1])