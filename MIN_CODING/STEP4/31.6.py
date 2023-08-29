arr = [1,2,3,3,5,1,0,1,3]
n = 9
k = int(input())
Sum = 0

for i in range(k):
    Sum += arr[i]

min_v = Sum

for i in range(n-k):
    Sum += arr[i+k]
    Sum -= arr[i]

    min_v = min(min_v,Sum)

print(min_v)

