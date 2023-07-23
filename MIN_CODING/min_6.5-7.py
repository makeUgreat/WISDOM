ch1, ch2 = input().split()

def trans_chr(ch):
    if 97 <= ord(ch) <= 122:
        ch = ch.upper()
    
    elif 65 <= ord(ch) <= 90: 
        ch = ch.lower()
    
    return ch

print(trans_chr(ch1), trans_chr(ch2)) 

    