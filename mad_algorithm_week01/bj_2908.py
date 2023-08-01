import sys
sys.stdin = open("BAEKJOON/for_min_input.txt", "r")


n1, n2 = input().split()
num_list = []

def reverse(strings):
    num_list.clear()
    for i in range(len(strings)):
        num_list.append(strings[i])
        
    reversed_str = num_list[-1] + num_list[1] + num_list[0]
    return int(reversed_str)

if reverse(n1) > reverse(n2):
    print(reverse(n1))
elif reverse(n1) < reverse(n2):
    print(reverse(n2))

