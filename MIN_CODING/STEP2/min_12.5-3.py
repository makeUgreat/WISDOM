def find():
    ch1 = input()
    
    flag = False
    for lst in lsts:
        if ch1 in lst:
            flag = True

    if flag:
        print("존재")
    else:
        print("없음")
            
    
    
lsts = [
    ['D','A','D'],
    ['Q','W','Q'],
    ['A','S','D'],
    ['A','S','D']
]

find()
