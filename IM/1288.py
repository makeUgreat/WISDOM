import sys
sys.stdin = open('input.txt','r')

for tc in range(1,int(input())+1):

    N = int(input())

    n = 0
    nums = []
    num_set = 0
    while 1:
        n += 1

        result = (N*n)  #1200
        len_list = []
        for i in str(result):
            len_list.append(i)


        for i in range(len(len_list)):
            nums.append(len_list[i])

        num_set = set(nums)

        if len(num_set) == 10:
            break

    print(f'#{tc} {N*n}')