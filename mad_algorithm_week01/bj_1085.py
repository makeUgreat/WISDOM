# 현수의 위치 x,y
# 오른쪽 위 꼭짓점 w,h

x,y,w,h = map(int,input().split())
distance = []


if 1 <= w <= 1000 and 1 <= h <= 1000:
    if 1 <= x <= w-1 and 1 <= y <= h-1:  #유효성 조건 x,y = 1~999  w,h = 1~1000
        
        
        if x < w-x:                 # 현수 to x축 거리가 현수 to 꼭짓점 x축 까지 거리보다 짧으면
            distance.append(x)       # x를 리스트에 추가 
        else:                       # 반대면 
            distance.append(w-x)  # 현수 to 꼭짓점거리를 리스트에 추가 
            
        if y < h-y:
            distance.append(y)
        else:
            distance.append(abs(h-y))

print(min(distance))
