# Loop Statement, 반복문
주어진 코드 블록을 여러 번 반복해서 실행하는 구문

1) for, 특정 작업을 반복적으로 수행
2) While, 주어진 조건이 참인 동안 반복


## for
임의의 시퀀스의 항목들을
그 시퀀스에 들어있는 순서대로 반복

```
for 변수 in 반복 가능한 객체:
    코드 블록
```

## iterable, 반복 가능한 객체
반복문에서 순회할 수 있는 객체
(시퀀스 객체 뿐만 아니라 dict,set 포함)


### 리스트의 요소가 아닌 인덱스로 접근하여 해당 요소들을 변경하기
```
numbers = [4, 6, 10, -8, 5]

for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2

print(numbers)
```


### 중첩 반복문
```
outers = ['A','B']
inners = ['c','d']

for outer in outers:
    for inner in inners:
        print(outer, inner)
```

안쪽 반복문은 outers 리스트의 각 항목에 대해 한번 씩 실행됨

print가 호출되는 횟수 => len(outers) * len(inners)




## while
주어진 조건식이 참인동안 코드를 반복해서 실행
== 조건식이 거짓(False)가 될 때 까지 반복 

```
a = 0

while a < 3:
    print(a)
    a += 1

print('끝')

```

### for vs while

### for
 - 반복 횟수가 명확하게 정해져 있는 경우에 유용
 - 예를 들어 리스트, 튜플, 문자열 등과 같은 시퀀스 형식의 데이터를 처리할 때

### while
- 반복 횟수가 불명확하거나 조건에 따라 반복을 종료해야할 때
- 예를 들어 사용자의 입력을 받아서 특정 조건이 충족될 때 까지 반복


