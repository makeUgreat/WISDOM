'''
map(function, iterable)
순회 가능한 데이터구조(iterable)의 모든 요소에 함수를 적용하고,
그 결과를 map object로 반환

'''
def my_func(x):
    result = x * 2
    return result

numbers = [1, 2, 3]
result = map(str, numbers)

print(result)
print(list(result))
######
result = []
for number in numbers:
    result.append(str(number))  # 이 반복문이 map과 똑같은 기능

print(result)


