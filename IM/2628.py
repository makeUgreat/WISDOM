import sys
sys.stdin = open('input.txt', 'r')

m, n = map(int, input().split())  # m가로 n 세로
nums = int(input())

r_list = [0, n]
c_list = [0, m]
for _ in range(nums):
    p, tip = map(int, input().split())

    if p == 0:
        r_list.append(tip)
    if p == 1:
        c_list.append(tip)

r_list.sort()
c_list.sort()

r_max = -21e8
c_max = -21e8
for i in range(1, len(r_list)):
    if r_list[i] - r_list[i - 1] > r_max:
        r_max = r_list[i] - r_list[i - 1]

for k in range(1, len(c_list)):
    if c_list[k] - c_list[k - 1] > c_max:
        c_max = c_list[k] - c_list[k - 1]


print(r_max*c_max)
