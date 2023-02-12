n=int(input())
m=int(input())

parent=[0]*(n+1)

for i in range(1,n+1):
    parent[i]=i

a=[list(map(int,input().split())) for _ in range(n)]

def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

for i in range(n):
    for j in range(n):
        if a[i][j]==1:
            if find_parent(parent,i+1)!=find_parent(parent,j+1):
                union_parent(parent,i+1,j+1)

ans=True
data=list(map(int,input().split()))
for i in range(m-1):
    if find_parent(parent,data[i])!=find_parent(parent,data[i+1]):
        ans=False
if ans:
    print("YES")
else:
    print("NO")