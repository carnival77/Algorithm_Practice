import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

n=int(input())
tree=[[] for _ in range(n)]
visited=[False]*(n)
ans=0
data=list(map(int,input().split()))
root=0
delete=int(input())

for child,parent in enumerate(data):
    if parent==-1:
        root=child
    else:
        tree[child].append(parent)
        tree[parent].append(child)

if root==delete:
    print(0)
    sys.exit(0)

def dfs(parent):
    global ans
    children_num=0
    visited[parent]=True
    for child in tree[parent]:
        if not visited[child] and child!=delete:
            children_num+=1
            dfs(child)
    if children_num==0:
        ans+=1

dfs(root)

print(ans)