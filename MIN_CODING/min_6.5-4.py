ch1 = input() 
asci = ord(ch1)
if 97 <= asci <= 122:
    print("소문자입력!!")
elif 65 <= asci <= 90:
    print("대문자입력!!")
elif 49 <= asci <= 57:
    print("숫자문자입력!!")