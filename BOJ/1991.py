import sys
sys.stdin = open('input.txt','r')

n = int(input())
tree = {}

for _ in range(n):
    root, right, left = input().split()
    tree[root] = [right,left]


# 이진트리.. 항상 왼쪽부터 탐색
def preorder(root):
    if root != ".":

        #노드에 들어오마자자 출력
        print(root,end='')
        preorder(tree[root][0])
        preorder(tree[root][1])

def inorder(root):
    if root != ".":

        # 오른쪽 노드 진입하기전에 출력
        inorder(tree[root][0])
        print(root,end="")
        inorder(tree[root][1])

def postorder(root):
    if root != ".":

        # 가장 깊은곳에서 반환하면서 출력
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root,end="")



preorder('A')
print()
inorder('A')
print()
postorder('A')