# lsts =[ ]
# bucket = [0] * 10

# for _ in range(3):
#     line = list(map(int,input().split()))
    
#     for i in range(len(line)):
#         bucket[line[i]] += 1



# for i in range(1,len(bucket)):
#     if bucket[i] == 0:
#         print(i,end=' ')


lsts = []
for _ in range(3):
    lsts.extend(map(int,input().split()))

bucket = {}

for ls in lsts:
    bucket[ls] += bucket.get(1,0)


for num in range(1,10): # 1~9 
    if num not in bucket:
        print(num,end=' ')