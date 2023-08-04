cardlist = list(input())
bucket = {}

for card in cardlist:
    bucket[card] = bucket.get(card,0) + 1 # 버켓 딕셔너리, card키의 값을 가져오고 거기에 1을 더해서 다시 card키의 값으로 더한다. 없으면 0을 반환해 1을 더한다

cnt = 0
for key in bucket.keys():
    cnt += 1

print(f'{cnt}개')