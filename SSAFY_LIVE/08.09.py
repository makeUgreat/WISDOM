# 순열은..  중복이 없고 순서가 있음.
# 하

card_set = 3 
cards = ['A','B','C','D']
path = [''] * card_set 

# 3개의 픽에 4개의 경우의 수니까 
# level = 3 

def abc(level):

    if level == card_set:
        for i in range(card_set):
            print(path[i],end=' ')
        print()
        return
    
    for i in range(4):
        if level > 0 and path[level-1] >= cards[i]: continue
        path[level] = cards[i]
        abc(level+1)
abc(0)