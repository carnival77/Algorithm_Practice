import sys
input=sys.stdin.readline

n,m=map(int,input().split())
ans=m

targets=list(map(int,input().split()))
targets.pop(0)

parent=[0]*(n+1)

for i in range(1,n+1):
    parent[i]=i

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

data=[]
for _ in range(m):
    row=list(map(int,input().split()))
    cnt=row.pop(0)
    if cnt>1:
        for i in range(1,cnt):
            if find_parent(parent,row[i])!=find_parent(parent,row[i-1]):
                union_parent(parent,row[i],row[i-1])
    data.append(row)

for row in data:
    ok=False
    for i in row:
        for j in targets:
            if find_parent(parent,i)==find_parent(parent,j):
                ans-=1
                ok=True
                break
        if ok:
            break

print(ans)