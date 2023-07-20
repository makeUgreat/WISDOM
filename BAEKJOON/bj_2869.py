# 낮 이동거리 A m 
# 밤에 내려가는 거리 B m
# 나무 높이 V m 
a, b, v = map(int,input().split())


velocity_per_day = a - b
need_days = (v / velocity_per_day) - (b/(a-b))

if v % velocity_per_day != 0:
    print( round(need_days+0.001) + 1)
else:
    print( round(need_days + 0.001) )

