n,m=map(int,input().split())
res=0
last=0

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

parent=[0]*(n+1)

for i in range(1,n+1):
    parent[i]=i

edges=[]
for _ in range(m):
    a,b,cost=map(int,input().split())
    edges.append((cost,a,b))

edges.sort()

for cost,a,b in edges:
    if find_parent(parent,a)!=find_parent(parent,b):
        union_parent(parent,a,b)
        res+=cost
        last=cost
print(res-last)