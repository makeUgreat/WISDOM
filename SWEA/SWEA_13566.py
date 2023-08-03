import sys
sys.stdin = open("input.txt","r")


T = int(input())

for tc in range(1,T+1):
    bucket = [0] * 10
    card_nums = int(input())
    cards = list(map(int,input()))

    for i in range(card_nums):
        bucket[cards[i]] += 1

    max_v = -21e8
    max_index = 0
    for element in bucket: # 버켓의 숫자는 갯수임
        if element >= max_v:
            max_v = element  #  max_v는 가장 많은 카드의 갯수

    max_num = 0
    for k in range(9,-1,-1):
        if bucket[k] == max_v:
            max_num = k
            break

    print(f'#{tc} {max_num} {max_v}')

