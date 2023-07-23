id, pw = map(int,input().split())

if id == 1111 and pw == 2222:
    print('로그인성공')
elif id != 1111:
    print('아이디가 틀렸습니다')
elif id == 1111 and pw != 2222:
    print('비밀번호가 틀렸습니다')
    
    
#GPT 
id, pw = map(int, input().split())

if id == 1111 and pw == 2222:
    print('로그인 성공')
elif pw != 2222:
    print('비밀번호가 틀렸습니다')
else:
    print('아이디가 틀렸습니다')
