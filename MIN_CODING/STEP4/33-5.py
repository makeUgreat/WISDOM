import sys
sys.stdin = open('input.txt','r')
N = int(input()) # 국가 수
population = list(map(int, input().split())) # 각 국가별 인구
K = int(input()) # 사건 수

# def populationFindSum(get_node):
#     Sum = 0
#    if parent[get_node] == 0:
#        Sum += get_node


def findP(get_node):
    if parent[get_node] == 0:
        return get_node

    else:
        res = findP(parent[get_node])
        return res


def alliance(x,y):
    root_x = findP(x)
    root_y = findP(y)

    if root_x == root_y:
        return

    else:
        parent[root_y] = root_x

parent = [0]*71
for n in range(K):
    Sum1_list = []
    Sum2_list = []
    order,x,y = input().split()
    x = population[ord(x)-65]
    y = population[ord(y)-65]

    if order == 'alliance':
        alliance(x,y)
        # print(f'n번째: {parent}')

    if order == 'war':
        for num in population:
            if findP(num) == findP(x):
                Sum1_list.append(num)
            elif findP(num) == findP(y):
                Sum2_list.append(num)

        if sum(Sum1_list) > sum(Sum2_list):
            loser = Sum2_list
        elif sum(Sum1_list) < sum(Sum2_list):
            loser = Sum1_list

        for nation in loser:
            population.remove(nation)


print(len(population))
