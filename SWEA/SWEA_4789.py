import sys
sys.stdin = open('input.txt','r')

for tc in range(1,int(input())+1):
    audi = list(map(int,input()))

    for i in range(len(audi)):  # i = 3
        now_clap = 0


        more_people = max(0,i - now_clap)




    print(f'#{tc} {more_people}')

    for T in range(int(input())):
        n = list(map(int, input()))
        cnt = 0
        for i in range(len(n)):
            clap = cnt + sum(n[:i])
            if clap < i:
                cnt += (i - clap)
        print(f'#{T + 1} {cnt}')