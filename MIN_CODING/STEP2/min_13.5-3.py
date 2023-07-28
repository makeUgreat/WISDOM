import sys
sys.stdin = open("MIN_CODING/input.txt","r")

line_a = list(map(int,input().split()))
line_b = list(map(int,input().split()))
line_c = list(map(int,input().split()))


for i in range(5):
    print(line_a[i] * line_b[i] + line_c[i], end=' ')