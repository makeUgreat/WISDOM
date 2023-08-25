import sys
sys.stdin = open('input.txt','r')

N = int(input()) # 시험장 갯수
A = list(map(int, input().split())) # 각 시험장마다 응시인원
B,C = map(int,input().split()) # 총 감독관 감시인원, 부감독관 ""

B_cnt = N
C_cnt = 0
for people in A:

    # 인원에서 총감독관 커버를 뺀다
    res = people-B
    if res <= 0: # 그 값이 0보다 작으면 총감독관만으로 커버 가능하므로 아래는 무시
        continue

    C_cnt += res // C # 남은 인원을 부감독관 커버 인원으로 채우고
    if res % C != 0: # 만약 남는 인원이 있으면
        C_cnt += 1 # 부감독관 한명 추가


print(B_cnt+C_cnt)



