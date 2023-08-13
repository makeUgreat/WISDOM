original = [
    ['A','B','C','D'],
    ['B','B','A','B'],
    ['C','B','A','C'],
    ['B','A','A','A']
]

get_arr = []
for _ in range(4):
    line = list(input())
    get_arr.append(line)

name = ['A','B','C','D']
big_cnt = -21e8
toomany = 0

for n in name:
    cnt = 0
    for i in range(4):
        for j in range(4):
            if get_arr[i][j] == original[i][j] == n:
                    cnt += 1
    if cnt > big_cnt:
        big_cnt = cnt
        toomany = n  
                
        

print(toomany)