x,y,w,h = map(int,input().split())
minimum = []

if 1 <= w <= 1000 and 1 <= h <= 1000:
    if 1 <= x <= w-1 and 1 <= y <= h-1:  #유효성 조건 x,y = 1~999  w,h = 1~1000
        
        
        if x < w-x:                
            minimum.append(x) 
        else:
            minimum.append(abs(w-x))  
            
        if h < h-y:
            minimum.append(h)
        else:
            minimum.append(abs(h-y))

print(min(minimum))
