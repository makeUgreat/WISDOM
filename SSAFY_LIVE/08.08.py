# 주사위 n개를 던졌을 때 (입력)
# 나올 수 있는 모든 경우의 수를 출력하시오. 

# branch = 6 (주사위 눈 1~6)
# level = n 

n = int(input())
path = [0] * n  # 주사위 개수

def abc(level):

    if level == n:
        for i in range(n):
            print(path[i],end=' ')
        print()
        return
    
    for i in range(6):
        path[level] = i + 1
        abc(level+1)

abc(0)