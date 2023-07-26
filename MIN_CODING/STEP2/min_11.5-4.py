lsts = [
    ['a','b','a','c','z'],
    ['c','t','a','c','d'],
    ['c','c','c','c','a']
]

ch1 = input()
count = 0
for lst in lsts:
    count += lst.count(ch1)
    
if count >= 7:
    print("세상에")
elif count >= 5:
    print("와우")
elif count >= 3:
    print("이야")
else:
    print()
    