import sys
sys.stdin = open("BAEKJOON/for_min_input.txt", "r")

def made_avg(n,*scores):
    total = sum(scores)
    avg = total / n
    count = 0
    for score in scores:
        if score > avg:
            count += 1
            
    return count / n * 100


C = int(input())
for i in range(C):
    n, *scores = map(int,input().split())
    average_ratio = made_avg(n,*scores)
    print(f'{average_ratio:.3f}%')
    