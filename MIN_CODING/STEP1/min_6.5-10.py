ch1, ch2, ch3 = map(ord,input().split())

if ch1 > ch2 and ch1 > ch3: 
    print(f'옳다{chr(ch1)}')
    
else:
    print('옳지않음')