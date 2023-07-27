def Process(user_input):
    user_input = user_input.lower()

    flag = False

    for lst in lsts:
        if user_input in lst:
            flag = True

    if flag:
        print("존재")
    else:
        print("없음")


lsts = [
    ['a','b','d'],
    ['e','w','z'],
    ['q','v','a']
]


user_input = input()
Process(user_input)