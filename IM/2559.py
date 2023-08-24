import sys
sys.stdin = open('input.txt','r')

N,K = map(int, input().split())

thermo = list(map(int, input().split()))


Sum = 0

# K만큼의 합 저장해놓고

for i in range(K):
    Sum += thermo[i]

Max = Sum

for i in range(N-K): # N-K =5 , 0 1 2 3 4
    Sum -= thermo[i]
    Sum += thermo[i+K]

    if Sum > Max:
        Max = Sum

print(Max)
