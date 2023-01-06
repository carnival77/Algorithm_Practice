import sys
input=sys.stdin.readline

n=int(input())
m=int(input())

# 집합은 0~n+1 번 집합이 있다. 0번 집합은 임의로 있다고 가정한다.
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

ans=0
for _ in range(m):
    data=find_parent(parent,int(input()))
    # 집합의 루트가 0이면, 더 이상 도킹이 불가능하다.
    if data==0:
        break
    # 새롭게 비행기가 도킹이 되면, 해당 집합을 바로 왼쪽의 집합과 합친다. 이 때, 번호가 0인 집합과도 합친다.
    union_parent(parent,data,data-1)
    ans+=1


print(ans)