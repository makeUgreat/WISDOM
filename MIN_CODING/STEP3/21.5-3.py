def draw(index):
    global st

    if not (index-1) < 0:
        st[index-1] = '#'
    
    if not (index+1) > len(st)-1:
        st[index+1] = '#' 


st = list(input())
s1, s2 = input().split()

st1_index = st.index(s1)
st2_index = st.index(s2)

draw(st1_index)
draw(st2_index)
    

print(*st,sep='')