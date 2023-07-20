a = [[10,20], [30,40], [50,60]]

#for 한번만 써서
for x,y in a:
    print(x,y)
print('-----')
#for문 2개 써서 
for i in a:
    for j in i:
        print(j, end= ' ')
    print()
print('-----')
#for문 range 써서
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()
print('-----')
#while 이용해서
i = 0
while i < len(a):
    x, y = a[i]  
    #2차원 배열에서 1차원 인덱스([]하나)로 부르면 [x,y] 리스트 자체를 불러옴
    #그래서 리스트 안에 요소(x,y)를 각각 x와 y에 선언(=)할 수 있음
    #인덱스를 2차원으로([][]처럼)하면 리스트 안에 요소에 직접 접근
    print(x, y)
    i += 1
print('-----')

#while 반복문 2번 사용
i = 0
while i < len(a): #세로크기
    j = 0
    while j < len(a[i]): #가로크기
        print(a[i][j], end=' ')
        j += 1
    print()
    i += 1

