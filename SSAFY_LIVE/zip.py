'''
zip(*iterables)  
임의의 iterable을 모아 튜플을 원소로 하는 zip object를 반환

'''

girls = ['jane', 'ashley']
boys = ['peter', 'jay']
pair = zip(girls,boys)

print(pair)
print(list(pair))

# zip

names = ['Alice', 'Bob', 'Charlie']
ages = [30, 25 ,35]
cities = ['New york','London', 'Paris']

for name, age, city in zip(names,ages,cities): # 0행 이면 0행끼리 1행이면 1행 요소끼리 각각 묶어서
    print(name, age, city)
    print(f'{name} is {age} years old and lives in {city}.')
print('-------------------')

for name, age, city in names,ages,cities: # 그런거 알빠 아니고 0행부터 아래로 주욱 
    print(name, age, city)
    print(f'{name} is {age} years old and lives in {city}.')