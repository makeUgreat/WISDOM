lsts = [
    ['A','B','C','D','E'], 
    ['E','A','B','A','B'], 
    ['A','C','D','E','R']
]

ch1 = input()
result = 0 

for i in range(len(lsts)):
    result += lsts[i].count(ch1)

if result >= 3:
    print("대발견")
elif 1 <= result <= 2:
    print("발견")
elif result == 0:
    print("미발견")