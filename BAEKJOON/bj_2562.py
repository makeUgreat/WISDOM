import sys
sys.stdin = open("input.txt", "r")

list = []
for i in range(9):
    x = int(input())
    list.append(x)


print(max(list))
print(list.index( max(list) )+1)