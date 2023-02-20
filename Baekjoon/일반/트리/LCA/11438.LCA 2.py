import sys
from collections import deque
input=sys.stdin.readline
print=sys.stdout.write

n=int(input())
tree=[[0] for _ in range(n+1)]

for _ in range(n-1):
    a,b=map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

kmax=0
temp=1

# 최대 가능 depth인 kmax 구하기. kmax는 트리의 높이 n>=2^k인 k의 최대값
while temp<=n:
    temp<<=1
    kmax+=1

depth=[0]*(n+1) # 노드 깊이 리스트
parent=[[0]*(n+1) for _ in range(kmax+1)] # 노드 조상 리스트. kmax 만큼의 행과 n개 노드 개수만큼의 열을 가짐.
visited=[False]*(n+1) # 노드 방문 체크 리스트

def bfs(node):
    q=deque()
    q.append(node)
    visited[node]=True
    level=1 # 트리 깊이
    now_size=1 # 현재 깊이에서 트리 노드 개수
    count=0 # 현재 깊이에서 방문한 트리 노드 개수
    while q:
        now=q.popleft()
        for next in tree[now]:
            if not visited[next]:
                visited[next]=True
                q.append(next)
                depth[next]=level # depth 리스트에 현재 깊이 저장
                parent[0][next]=now # parent 리스트의 첫 번째 열(2^0, 즉 바로 위의 부모)에 자신의 부모 노드 저장
        count+=1 # 방문한 트리 노드 개수 증가
        if now_size==count: # 현재 깊이의 모든 노드 방문했으면
            count=0 # count 초기화
            now_size=len(q) # 방문할 트리 노드 개수
            level+=1 # 현재 depth 1 증가

bfs(1)

# parent 리스트 값 2^k번째 부모 노드 계산 및 저장하여 채우기.
# 점화식 : P[K][N]=P[K-1][P[K-1][N]]
for k in range(1,kmax+1): # 2^k번째 부모 노드 계산 및 저장
    for n in range(1,n+1): # 노드 개수 n만큼 반복
        parent[k][n]=parent[k-1][parent[k-1][n]]

# LCA 함수 구현
def executeLCA(a,b):
    # a 노드가 b 노드보다 depth 가 더 작도록 설정. a 노드가 depth 가 더 크면, a 노드와 b 노드를 교체.
    if depth[a]>depth[b]:
        a,b=b,a

    # 두 노드의 depth를 동일하게 맞추기(높이가 맞을 때까지 a를 부모 노드로 변경). parent 리스트를 활용해 2의 k제곱수 단위로 이동
    # k를 kmax부터 0까지 1씩 줄여가며 탐색
    for k in range(kmax,-1,-1):
        # b 노드와 a 노드의 깊이의 차이보다 작거나 같은 2의 k제곱수이며,
        # b 노드의 해당 수의 부모 노드의 깊이가 a 노드 깊이보다 크거나 같다면
        if pow(2,k)<=depth[b]-depth[a] and depth[a]<=depth[parent[k][b]]:
            # b 노드를 2의 k제곱수의 부모 노드로 변경하여 두 노드의 depth를 동일하게 맞춘다
            b=parent[k][b]

    # 공통 조상 찾기. 두 노드의 공통 조상이 나오거나 k가 0이 될 때까지 각 노드를 부모 노드로 변경 반복.
    # parent 리스트를 활용해 2의 k제곱수 단위로 이동
    for k in range(kmax,-1,-1):
        # 두 노드가 같다면 공통 조상을 찾은 것이므로 탐색 중지
        if a==b: break
        # 두 노드의 2의 k제곱수만큼의 부모 노드가 다르다면, 2의 제곱수만큼 부모 노드로 이동
        if parent[k][a]!=parent[k][b]:
            a=parent[k][a]
            b=parent[k][b]

    # 반복문이 종료된 후 이동한 2개의 노드가 같은 노드라면 해당 노드가,
    # 다른 노드라면 바로 위의 부모 노드가 최소 공통 조상이 된다.
    LCA=a
    if a!=b:
        LCA=parent[0][LCA]

    return LCA

m=int(input())

for _ in range(m):
    a,b=map(int,input().split())
    print(str(executeLCA(a,b)))
    print("\n")