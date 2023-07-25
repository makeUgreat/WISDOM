
def output(ch1, ch2):
    if ch1.isupper() and ch2.isupper():
        print("대문자들")
    elif ch1.isupper() or ch2.isupper():
        print("대소문자")
    else:
        print("abcdefghijklmnopqrstuvwxyz")
        
        
ch1, ch2 = input().split()

output(ch1, ch2)
