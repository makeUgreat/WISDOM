# level = 5
# branch = 5

nums = list(map(int,input().split()))
path = [0] * 5
visit = [False] * 5
min_v = 21e8
max_v = -21e8
def abc(level):
    global min_v, max_v
    if level == 5:
        result = path[0] * path[1] - path[2] * path[3] + path[4]

        if result < min_v:
            min_v = result
        if result > max_v:
            max_v = result
        return

    for i in range(5):
        if not visit[i]:
            visit[i] = True
            path[level] = nums[i]
            abc(level+1)
            visit[i] =False

abc(0)
print(max_v)
print(min_v)

