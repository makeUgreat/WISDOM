import sys
sys.stdin = open('input.txt','r')


for _ in range(int(input())):

    line = list(map(int, input().split()))
    tc = line[0]
    cnt = 0
    new_line = []

    for i in range(1,21):
        now = line[i] # 줄에 넣을 아이 키
        flag = 0

        # 처음은 그냥 추가
        if len(new_line) == 0:
            new_line.append(now)

        # 다음 아이부터 앞에 있는 아이들과의 키를 비교
        else:
            for student in new_line:
                if student > now: #학생이 넣을 아이보다 키가 더 크면
                    stu_idx = new_line.index(student) # 학생이 있던 자리를 찾고
                    cnt += len(new_line[stu_idx:])
                    new_line.insert(stu_idx, now)
                    flag = 0
                    break
                flag = 1

        if flag:
            new_line.append(now)

    print(f'{tc} {cnt}')



