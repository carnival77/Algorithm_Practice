import sys

input = sys.stdin.readline

n,m= map(int,input().split())

parent=[0]*(n+1) # 부모 테이블 (총 노드 개수 + 1 ) 초기화

# 부모 테이블에서 자기 자신을 부모로 초기화
for i in range(n+1):
    parent[i]=i

# 특정 원소가 속한 집합을 찾기
def find_parent(x):
    # 루트 노드가 맞다면 그대로 리턴
    if parent[x]==x:
        return x
    # 루트 노드가 아니라면, 루트 노드를 찾울 때까지 재귀적으로 호출
    parent[x] = find_parent(parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(a,b):
    # 각각의 부모 루트 노드 찾기
    a=find_parent(a)
    b=find_parent(b)

    # 유의사항! 이것은 트리를 구성하는 것이 아닌 단순히 합집합을 하는 것이기에, 크기 비교 안 해도 된다.
    if a!=b:
        parent[b]=a
    # if a<b:
    #     parent[b]=a
    # else:
    #     parent[a]=b

for _ in range(m):
    op,a,b = map(int,input().split())
    if op==0:
        union_parent(a,b)
    else:
        if find_parent(a) == find_parent(b):
            print('YES')
        else:
            print('NO')