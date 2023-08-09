ID = input()
PASSWORD = input()


def check(get_id, get_password):

    if get_id == "qlqlaqkq" and get_password == "tkaruqtkf":
        return 1    
    return 0



if check(ID,PASSWORD):
    print('LOGIN')
else: print("INVALID")