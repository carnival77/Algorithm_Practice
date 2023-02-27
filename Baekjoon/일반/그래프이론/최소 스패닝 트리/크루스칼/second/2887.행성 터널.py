import sys
input=sys.stdin.readline

n=int(input())

x=[]
y=[]
z=[]
parent=[0]*(n+1)

for i in range(1,n+1):
    parent[i]=i

for i in range(n):
    a,b,c=map(int,input().split())
    x.append([a,i])
    y.append([b,i])
    z.append([c,i])

x.sort()
y.sort()
z.sort()

edges=[]

for i in range(1,n):
    px,pxi=x[i-1]
    nx,nxi=x[i]
    edges.append((abs(px-nx),pxi,nxi))
    py,pyi=y[i-1]
    ny,nyi=y[i]
    edges.append((abs(py-ny),pyi,nyi))
    pz,pzi=z[i-1]
    nz,nzi=z[i]
    edges.append((abs(pz-nz),pzi,nzi))

edges.sort()

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

ans=0
for cost,a,b in edges:
    if find_parent(parent,a)!=find_parent(parent,b):
        union_parent(parent,a,b)
        ans+=cost

print(ans)