def input_func():
    ch1 = input()
    result = check(ch1)

    if result == 1:
        print("있음")
    elif result == 0:
        print("없음")

def check(ch1):
    
    for lst in lsts:
            if ch1 in lst:
                return 1
            elif ch1 not in lst:
                return 0
                



lsts = [
    ['D','A','C','C','D'],
    ['S','D','F','A','E'],
    ['E','E','T','J','H']
]


input_func()

