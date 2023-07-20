
# Control Statement, 제어문
코드의 실행 흐름을 제어하는데 사용되는 구문
조건에 따라 코드 블록을 실행하거나 반복적으로 코드를 실행



## Conditional Statement, 조건문
주어진 조건식을 평가하여 해당 조건이 참(True)인 경우에만 
코드 블록을 실행하거나 건너뜀


### if 
```
if 표현식:
    코드 블록
elif 표현식:
    코드 블록
else:
    코드 블록
```
### 조건문의 예시
```
a = 5
if a > 3:
    print('3 초과')
else:  # if가 거짓일 경우만 실행
    print('3 이하')
print(a)

``` 

### elif, 복수 조건문 예시

```
# 순차적으로 비교

dust = 35

if dust > 150:
    print('매우 나쁨')
elif dust > 80: # 위 if가 False일 때만 실행
    print('나쁨')
elif dust > 30: # 위 elif가 False일 때만 실행
    print('보통')
else:
    print('좋음')


```


### 중첩 조건문 예시
```
dust = 480
if dust < 150:
    print('매우 나쁨')
    if dust > 300:  #dust가 300초과면 위험해요 나가지 마세요'도' 출력
        print('위험해요! 나가지 마세요!')
elif dust > 80:
    print('나쁨')
elif dust > 30:
    print('보통')
else:
    print('좋음')

```