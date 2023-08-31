import sys
sys.stdin = open('input.txt','r')
'''
같은 등급 -> union
n번 고기는 x등급 입니다 -> 보스설정
'''
def findP(get_node):
    if parent[get_node] == 0:
        return get_node

    else:
        res = findP(parent[get_node])
        return res


def union(a,b):

    root_a = findP(a)
    root_b = findP(b)

    if root_a == root_b:
        return

    if root_a >= 65:
        parent[root_b] = root_a

    if root_b >= 65:
        parent[root_a] = root_b

    else:
        parent[root_b] == root_a

N,K = map(int,input().split()) # 품목갯수, 고기갯수

parent = [0]*200
parent[2] = ord('B')
parent[3] = ord('B')
parent[4] = ord('B')

for _ in range(N):
    a,b = input().split()

    if a.isdigit() and b.isdigit(): # a나 b 둘다 숫자면
        union(int(a),int(b))

    else:
        if a.isdigit(): # a만 숫자면
            union(int(a),ord(b))

        elif b.isdigit(): # b만 숫자면
            union(ord(a),int(b))


for num in parent:
    if num != 0:
        print(chr(num),end='')