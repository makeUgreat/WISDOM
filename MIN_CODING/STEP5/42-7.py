dict ={
    'a': 15,
    'b': 20,
    'c': 44,
    'd':22,
    'e':55,
    'f':16,
    'g':45
}

st= list(input())
n = int(input()) #제외할 물건
visit = [False] * len(st)

max_v = -21e8
def abc(level,Sum):
    global max_v    
    
    if level == (len(st)-n): 
        if Sum % 10 == 0:
            if Sum > max_v:
                max_v = Sum
        
        return
    
    for i in range(len(st)):
        if not visit[i]:
            visit[i] = True
            abc(level+1, Sum + dict[st[i]]) 
            visit[i] = False
    
abc(0,0)
print(max_v)