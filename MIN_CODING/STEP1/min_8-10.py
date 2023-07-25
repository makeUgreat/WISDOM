lst = [[4,3,1,1], [3,1,2,1], [0,0,1,2]]

num = int(input())
num_sum = 0

for i in range( len(lst) ):
    num_sum += lst[i].count(num)

print(f'{num_sum}개 존재합니다')