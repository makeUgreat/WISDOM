array = [[0 for _ in range(4)] for _ in range(3)]

def input_func():
    num = int(input())
    i, j = 0, 0
    while i < 3:
        while j < 4:
            array[i][j] = num
            num += 1
            j += 1
        j = 0
        i += 1

def process_func():
    i, j = 0, 0
    while i < 3:
        while j < 4:
            array[i][j] += 1
            j += 1
        j = 0
        i += 1

def output_func():
    i = 0
    while i < 3:
        print(*array[i])
        i += 1

# 메인 코드
input_func()
process_func()
output_func()