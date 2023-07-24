import sys
sys.stdin = open("MIN_CODING/input.txt", "r")

def guess_num(*args):
    for i in args:
        if i < 20:
            print("더 큰수를 입력하세요")
        elif i > 20:
            print("더 작은수를 입력하세요")
        else:
            print("정답입니다")

user_input = list(map(int,input().split()))
guess_num( *user_input )