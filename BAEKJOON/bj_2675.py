import sys
sys.stdin = open("BAEKJOON/input.txt", "r")

string_list = []
def repeat(num, *strings):
    for string in strings:
        for i in range(len(string)):
            print(string[i]*int(num),end='')
        print()
    
for i in range(int(input())):
    N, S = input().split()
    repeat(N,S)

