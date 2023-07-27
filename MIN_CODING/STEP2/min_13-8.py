def CompareGo(lsts_1, lsts_2):
    
    if lsts_1 == lsts_2:
        print("두배열은완전같음")
    else:
        print("두배열은같지않음")
        
lsts_1 = [3,5,1,2,7]
lsts_2 = list(map(int,input().split()))

CompareGo(lsts_1, lsts_2)