file = open('hello.txt','w')
file.write('Hello, world!')
file.close()


file = open('hello.txt','r')
s = file.read()
print(s)
file.close()

# 파일 자동닫기

with open('hello.txt','r') as file:
    s = file.read()
    print(s)


with open('hello.txt','w') as file:
    for i in range(3):
        file.write('Hello, world! {0}\n'.format(i))

lines = ['안녕하세요.\n', '파이썬\n', '코딩 도장입니다.\n']
with open('hello.txt','w') as file:
    file.writelines(lines)

with open('hello.txt', 'r') as file:
    lines = file.readlines()
    print(lines)

with open('hello.txt', 'r') as file:
    line = None
    while line != '':
        line = file.readline()
        print(line.strip('\n'))


with open('hello.txt', 'r') as file:
    for line in file:
        print(line.strip('\n'))