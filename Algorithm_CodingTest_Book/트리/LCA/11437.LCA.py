from collections import deque
import sys
input=sys.stdin.readline
print=sys.stdout.write

n=int(input())
tree=[[] for _ in range(n+1)]

for _ in range(n-1):
    a,b=map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

depth=[0]*(n+1) # 노드 깊이 리스트
parent=[0]*(n+1) # 노드 조상 리스트
visited=[False]*(n+1)

def bfs(node):
    q=deque()
    q.append(node)
    visited[node]=True
    level=1 # 트리 깊이
    now_size=1 # 현재 깊이에서의 트리 노드 개수
    count=0 # 현재 깊이에서 방문한 트리 노드 개수.
    while q:
        now=q.popleft()
        for next in tree[now]:
            if not visited[next]:
                visited[next]=True
                q.append(next)
                parent[next]=now # parent 리스트에 자신의 부모 노드 저장
                depth[next]=level # depth 리스트에 현재 깊이 저장
        count+=1 # 방문한 트리 노드 개수 증가
        if now_size==count: # 현재 깊이의 모든 노드 방문했으면
            count=0 # count 초기화
            now_size=len(q) # 방문할 트리 노드 개수
            level+=1 # 현재 depth 1 증가

bfs(1)

# LCA 함수 구현
def executeLCA(a,b):
    # a 노드가 b 노드보다 depth 가 더 작도록 설정. a 노드가 depth 가 더 크면, a 노드와 b 노드를 교체.
    if depth[a]>depth[b]:
        a,b=b,a

    # 두 노드의 depth를 동일하게 맞추기(높이가 맞을 때까지 b를 부모 노드로 변경)
    while depth[a]!=depth[b]:
        b=parent[b]

    # 공통 조상 찾기. 두 노드의 공통 조상이 나올 때까지 각 노드를 부모 노드로 변경 반복
    while a!=b:
        a=parent[a]
        b=parent[b]

    return a

m=int(input())

for _ in range(m):
    a,b=map(int,input().split())
    print(str(executeLCA(a,b)))
    print("\n")