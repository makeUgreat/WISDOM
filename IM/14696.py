import sys
sys.stdin = open('IM/input.txt','r')

def save(take,get_cards):
    # A 카드 저장 
    # take = 0 , A카드
    # take = 1, B카드
    for i in get_cards:
        if i == 4:
            card_set[0][take] += 1
        if i == 3:
            card_set[1][take] += 1
        if i == 2:
            card_set[2][take] += 1
        if i == 1:
            card_set[3][take] += 1
                   

N = int(input()) # 라운드

for tc in range(N):
    
    card_set = [[0] * 2 for _ in range(4)]

    
    A_cards = list(map(int, input().split()))
    B_cards = list(map(int, input().split()))
    
    A_card_len = A_cards.pop(0)
    B_card_len = B_cards.pop(0)
    
    save(0,A_cards)
    save(1,B_cards)
    
    result = 'D'
    for a,b in card_set:
        if a == b: 
            continue
        if a > b: 
            result = 'A'
            break
        if a < b: 
            result = 'B'
            break

 
    print(result)
        
        