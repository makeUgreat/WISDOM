'''
우선 행으로 입력받고
해당하는 행을 정렬한 뒤
90도 뒤집어서 출력한다
'''

box = [list(map(int,input())) for _ in range(5)]

L1,L2 = map(int,input().split())

box[L1].sort()
box[L2].sort()

ro_box = list(zip(*box))

print(*ro_box[0])