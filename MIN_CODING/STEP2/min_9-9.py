lsts = [
    ['F','E','W'],
    ['D','C','A']
]



def findCh(ch1):
    found = False
    for lst in lsts:
        if ch1 in lst:
            found = True
            break 
    if found:
        print('발견')
    else:
        print('미발견')

user_input = input()
findCh(user_input)