def isExist(get_pix, map_elements):

    # 출력이 pix의 2*2 배열이니까 
    # 출력하는 함수도 pix를 풀어야함 

    for row in get_pix:
        for element in row:
            if element == map_elements:
                print
  


map_ = [
    [3,55,42],
    [-5,-9,-10]
]

pix = []
for _ in range(2):
    line = list(map(int,input().split()))
    pix.append(line)


for row in map_:
    for col in row:
        isExist(pix,col)
        