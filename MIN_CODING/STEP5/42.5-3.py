def calc_one(a,b):
    return (a-b) * (a+b)

def calc_two(a,b):
    if a > b:
        return a
    if a < b:
        return b

def calc_three(a,b):
    return (a**2) - (b**2)

def calc_four(a,b):
    return (a+b)**2


N = int(input())
nums = list(map(int,input().split()))
what = [0]*N-1

def dfs(level):

    if level == N-1:
        return


    for i in range(N-1):
        what[level] =


