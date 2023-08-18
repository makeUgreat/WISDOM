hero = ['B','I','A','H']

cnt_i = 0
i = 0
target_num = int(input())

def sth(hero,cnt_i,target_num):
    global i
    while cnt_i < target_num:
        cnt_i += 1
        i = cnt_i % len(hero)

    if len(hero) <= 2:
        print(hero[i],end=' ')
        hero.pop(i)
    else:
        print(hero[i-1],end=' ')
        hero.pop(i-1)


for _ in range(4):
    sth(hero,cnt_i,target_num)
