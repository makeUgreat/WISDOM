a, b = map(int,(input().split()))

if 1 <= a <= 20 and 10 <= b <= 30:
    if a < b:
        list = [2**i for i in range(a, b+1)]
        list.pop(1)
        list.pop(-2)

        print(list)
        
            