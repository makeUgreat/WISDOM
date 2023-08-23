import sys
sys.stdin = open('IM/input.txt','r')

students = int(input())
number = map(int,input().split())

stu_list = []
for i in range(1,students+1):
    stu_list.append(i)

stuline = [0] * students
line = []
for student,num in zip(stu_list, number):
    # print(student, num)
    stuline.insert(num,student)
    # print(stuline)

stuline.reverse()
# print(stuline)

for i in stuline:
    if i != 0:
        print(i,end=' ')