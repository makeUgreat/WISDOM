import sys
sys.stdin = open("input.txt","r")

# 정렬하기 위해 요소를 정수로 리스트 생성

prices = [ int(i) for i in input().split(';') ]
prices.sort()
prices.reverse()

# 콤마 찍기 위해 다시 문자열로 변환
formatted_prices = [ format(price,',') for price in prices ]

for i in formatted_prices:
    print(i.rjust(9))



# join 메서드를 이용한 방법 
# prices = [int(i) for i in input().split(';')]
# prices.sort()
# prices.reverse()

# formatted_prices = ','.join(map(str, prices))
# print(formatted_prices)