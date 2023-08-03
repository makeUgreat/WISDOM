def isSame(get_password,safe_password): 
    for i in range(len(safe_password)):
        if len(get_password) != len(safe_password):
            return 0
        if get_password[i] != safe_password[i]:
            return 0
    else:
        return 1
    

safe_password = [3,7,4,9]
input_pass = list(map(int,input().split()))

if isSame(input_pass,safe_password):
    print('pass')
else:
    print('fail')

