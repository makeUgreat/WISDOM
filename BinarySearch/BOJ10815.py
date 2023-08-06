import sys
sys.stdin = open("BinarySearch/input.txt","r")

card_N = int(input())
cards = list(map(int,input().split()))
check_N = int(input())
checks = list(map(int,input().split()))

cards.sort()

def bs(array,target,start,end):
    while start <= end:
        mid = (start+end) // 2
        if array[mid] == target:
            return 1
        elif array[mid] > target:
            end = mid -1
        elif array[mid] < target:
            start = mid + 1
    return 0



for check in checks:
    if bs(cards,check,0,card_N-1):
        print(1,end=' ')
    else:
        print(0,end=' ')
        