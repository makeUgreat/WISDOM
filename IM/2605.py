import sys
sys.stdin = open('input.txt','r')

students = int(input())


line = []
for i in range(students):
    if i == 0:
        line.append(i+1)

    for j in range(0,students):
