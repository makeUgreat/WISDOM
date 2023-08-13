# vertex ... 원소 개수 = 8
# edge ..  7 

lst = [[] for _ in range(8)] # 인접리스트는 각 노드마다 가지고있으므로
# 노드 갯수만큼 리스트 생성(인접행렬처럼?)

# 노드와 그 인덱스들
name = ['A','B','C','D','E','F','G','H'] 

# 원소별 인접리스트 생성(8개 나와야..)
bro = input()
bro_index = -1
for i in range(len(name)):
    if name[i] == bro:
        bro_index = i # B -> 1

lst[0].append(1)  # A->B 
lst[0].append(7)  # A->H
lst[0].append(2)  # A->C
lst[2].append(3)  # C->D
lst[2].append(6)  # C->G
lst[2].append(4)  # C->E
lst[3].append(5)  # D->F

parent_index = -1
def dfs(now):
    global parent_index
    # if now = 1
        
    
    for i in lst[now]:
        if i == bro_index:
            parent_index = now
        dfs(i)
    
dfs(0)

if parent_index == -1:
    print("없음")
else:
    for node in lst[parent_index]:
        if node == bro_index: continue
        print(name[node],end=' ')