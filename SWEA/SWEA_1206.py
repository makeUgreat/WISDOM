import sys
sys.stdin = open('input.txt', 'r')


def building_set(index):
    height_lists = []

    height_lists.append(height_buildings[index - 2])
    height_lists.append(height_buildings[index - 1])
    height_lists.append(height_buildings[index])
    height_lists.append(height_buildings[index + 1])
    height_lists.append(height_buildings[index + 2])

    if height_buildings[index] >= max(height_lists):
        height_lists.sort()
        return height_buildings[index] - height_lists[3]
    else:
        return 0

for tc in range(1,11):  # 10개의 테스트 케이스가 주어진다
    num_buildings = int(input())  # 건물의 개수
    height_buildings = list(map(int, input().split()))
    good_views = 0  # 조망권 조건에 맞는 건물의 수
    for building in range(2, num_buildings-2):  # 건물의 개수만큼 순회
        good_views += building_set(building)


    print(f'#{tc} {good_views}')
