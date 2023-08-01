ch1, ch2 = input().split()

lsts = [
    ['A','B','K','T'],
    ['K','F','C','F'],
    ['B','B','Q','Q'],
    ['T','P','Z','F']
]

# 입력받은 문자가 배열에 있는지 체크
cnt = 0 # 있으면 카운팅
for lst in lsts:
    cnt += lst.count(ch1)
    cnt += lst.count(ch2)

print(cnt)
