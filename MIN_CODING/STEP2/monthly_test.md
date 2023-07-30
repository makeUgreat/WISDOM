### 딕셔너리 
https://dojang.io/mod/page/view.php?id=2307


### 재귀함수
 https://dojang.io/mod/page/view.php?id=2352


 ### 메서드 코드 
 ## sum
 ```
 def custom_sum(numbers):
    result = 0
    for num in numbers:
        result += num
    return result
 ```
 ## max
 ```
 def max(list):
    if not list:  # 리스트가 비어있을 경우 None 반환
        return None

    최대값 = list[0]
    for 값 in list:
        if 값 > 최대값:
            최대값 = 값

    return 최대값
 ```
 ## min 
 ```
 def min(list):
   if not list:  # 리스트가 비어있을 경우 None 반환
        return None

    최소값 = list[0]
    for 값 in list:
        if 값 < 최소값:
            최소값 = 값

    return 최소값
 
 ```
 ## len
```
def custom_len(arr):
    count = 0
    for item in arr:
        count += 1
    return count
```