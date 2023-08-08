Map = [
    ['A','B','G','K'],
    ['T','T','A','B'],
    ['A','C','C','D']
]


pattern = []
for _ in range(2):
    line = input()
    pattern.append(line)

def cntPattern(y,x): # 0,0 
    
    for i in range(2):
        for j in range(2):
            if Map[i+y][j+x] != pattern[i][j]:
                return 0
    return 1

cnt = 0
for i in range(2):
    for j in range(3):    
        if cntPattern(i,j):
            cnt += 1

if cnt:
    print(f'발견({cnt}개)')
else:    
    print(f'미발견')
