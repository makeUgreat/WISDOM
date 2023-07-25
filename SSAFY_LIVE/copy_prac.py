# 얕은 복사, 원본과 다른 새로운 객체를 생성하는 것

# 예시
# 슬라이싱
# .copy() 

a = [1, 2, 3]
b = a[:]
b[0] = 100
print(a, b)

# copy
c = a.copy()
c[0] = 100
print(a,c)


# 얕은 복사의 한계
a = [1, 2, [1, 2]]

b = a[:]
b[2][0] = 999

print('2차원 리스트 요소를 수정하면: ', a,b)

b[1] = 444
print('1차원 리스트 요소를 수정하면: ', a, b)





# 깊은 복사 
import copy

original_list = [1, 2, [1,2]]
deep_copied_lsit = copy.deepcopy(original_list)

deep_copied_lsit[2][0] = 999

print(original_list, deep_copied_lsit) # 2차원 리스트까지 복사해서 
# 2차원 리스트의 같은 주소를 참조하는 것을 방지 .

