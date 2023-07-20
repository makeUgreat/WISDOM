# 3차원 리스트 만들기
a = [ [ [0]*3 for row in range(4) ] for depth in range(2)]
print(a)


# 작은 차원부터 순서대로 만들기
# 예를 들어 높이2 세로4 가로3 의 3차원 배열을 만드려면
# 1차원인 가로3 '[0]*3' 부터 만들고 이후
# 2차원인 세로4 'for row in range(4) 이후
# 3차원인 높이2 'for depth in range(2) 

