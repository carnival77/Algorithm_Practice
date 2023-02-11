# 특정 원소가 속한 집합을 찾는다.
def find_parent(parent,x):
    # 특정 원소의 부모가, 스스로 부모인 루트 노드가 아니면, 부모가 있다는 뜻이므로, 부모 노드로 루트 노드를 찾아 더 이상 부모를 찾을 수 없을 때까지 재귀 호출한다.
    if parent[x]!=x:
        parent[x]=find_parent(parent,x)
    return parent[x]

# 두 원소가 속한 집합을 합친다.
def union_parent(parent,a,b):
    # 각 원소의 루트 노드를 찾는다.
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    # 루트 노드의 숫자가 더 작은 쪽이 합쳐진 집합의 새로운 루트 노드가 된다.
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

# 노드, 간선 개수 입력 받기
v,e = map(int,input().split())
parent = [0] * (v+1) # 부모 테이블 초기화

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1,v+1):
    parent[i] = i

# union 연산을 각각 수행
for i in range(e):
    a,b = map(int,input().split())
    union_parent(parent,a,b)

# 각 원소가 속한 집합 출력
print('각 원소가 속한 집합 : ',end=' ')
for i in range(1,v+1):
    print(find_parent(parent,i), end=' ')

print()

# 부모 테이블 내용 출력
print('부모 테이블 : ',end=' ')

for i in range(1,v+1):
    print(parent[i],end=' ')