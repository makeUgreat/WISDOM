n = int(input())
arr = list(map(int,input().split()))

k = 4
Sum = 0

for i in range(k):
    Sum += arr[i]

min_v = Sum

for i in range(n-k):
    Sum += arr[i+k]
    Sum -= arr[i]

    min_v = min(min_v,Sum)


print(min_v)

