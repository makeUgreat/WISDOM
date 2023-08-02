# 연속되는 숫자 3개의 합이 가장 클 때 의 값을 출력해 주세요
lsts = [[4, 5, 2, 6, 7, 3, 1],
      [2, 9, 9, 6, 1, 6, 7]]



for lst in lsts:
    tmp = []
    max_v = 0
    for i in range(len(lst)-3):
        sum_ = 0
        for j in range(i, i+3):
            sum_ += lst[j]
            tmp.append(sum_)
        max_v = max(tmp)
    print(max_v)