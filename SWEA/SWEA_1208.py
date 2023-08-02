import sys
sys.stdin = open("input.txt","r")

for tc in range(1,11):
    dumps = int(input())
    box_heights = list(map(int,input().split()))

    for _ in range(dumps):
        for i in range(len(box_heights)):
            if box_heights[i] == max(box_heights):
                box_heights[i] -= 1
                break

        for i in range(len(box_heights)):
            if box_heights[i] == min(box_heights):
                box_heights[i] += 1
                break


    GAP = max(box_heights) - min(box_heights)
    print(f'#{tc} {GAP}')

