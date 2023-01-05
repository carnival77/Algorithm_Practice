import math

v=int(input())
parents=[0]*(v+1)
edges=[]
ans=0

for i in range(1,v+1):
    parents[i]=i

points=[list(map(float,input().split())) for _ in range(v)]
edges=[]
for i in range(len(points)-1):
    x1,y1=points[i]
    for j in range(i,len(points)):
        x2,y2=points[j]
        dist = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))  # dist=cost
        edges.append((dist, i, j))

edges.sort()

def find_parent(parents,x):
    if parents[x]!=x:
        parents[x]=find_parent(parents,parents[x])
    return parents[x]

def union_parent(parents,a,b):
    a=find_parent(parents,a)
    b=find_parent(parents,b)
    if a<b:
        parents[b]=a
    else:
        parents[a]=b

for edge in edges:
    cost,a,b=edge
    if find_parent(parents,a)!=find_parent(parents,b):
        union_parent(parents,a,b)
        ans+=cost

print(round(ans,2))