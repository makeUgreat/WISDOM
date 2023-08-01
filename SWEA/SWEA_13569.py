T = int(input())
for tc in range(1, T+1): # 테스트케이스의 갯수
    width_room = int(input())  # 방의 가로 길이
    boxes_height = list(map(int,input().split())) # 상자들의 높이

    cnt_list = []
    index = 0
    for i in range(len(boxes_height)): # box = 각 박스별 높이
        cnt = 0
        for j in range(len(boxes_height)):
            if j > i:
                if boxes_height[i] > boxes_height[j]:
                    cnt += 1
        cnt_list.append(cnt)

    print(f'#{tc} {max(cnt_list)}')

#이미 센 박스 앞 박스만 세는 방법?
