
def go(v,e):
    parents=[0]*(v+1)
    edges=[]
    ans=0
    total=0

    for i in range(1,v+1):
        parents[i]=i

    for _ in range(e):
        a,b,cost=map(int,input().split())
        edges.append((cost,a,b))
        total+=cost

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

    print(total-ans)

while True:
    v, e = map(int, input().split())
    if (v,e)==(0,0):
        break
    else:
        go(v,e)