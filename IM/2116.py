import sys
sys.stdin = open('input.txt','r')


n = int(input())

dice = []
for i in range(n):
    row = list(map(int,input().split()))
    dice.append(row)


for i in range(n):
    if dice[n-1][n-1]