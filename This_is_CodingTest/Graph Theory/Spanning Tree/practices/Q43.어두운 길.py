n,m=map(int,input().split())

parent=[0]*(n+1)

for i in range(1,n+1):
    parent[i]=i

edges=[]

for _ in range(m):
    a,b,cost=map(int,input().split())
    edges.append((cost,a,b))

edges.sort()

def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]