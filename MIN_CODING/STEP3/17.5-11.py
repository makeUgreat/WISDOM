def masking(target):
    mask = list(map(int,input().split()))
    sum_ = 0
    for i in range(len(mask)):
        if mask[i] == 1:
            sum_ += target[i]
    return sum_

lst = [3,5,4,2]

print(masking(lst))