hero = ['B','I','A','H']
N = int(input())

start = 0
for _ in range(4):
    for i in range(start,start+N):
        idx = i % len(hero)
    # print(hero)
    start = idx
    print(hero.pop(idx),end=' ')


