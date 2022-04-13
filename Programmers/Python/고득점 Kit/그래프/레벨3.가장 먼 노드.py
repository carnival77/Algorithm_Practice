# 그래프 구현방식에는 인접행렬방식과, 인접리스트방식이 존재합니다.
# 인접행렬방식 : 한 정점과 연결된 모든 정점을 찾는 데 걸리는 시간 복잡도(효율성) : O(V)(한 정점에서 한 행 즉 V개수만큼 탐색)
# 장점은 임의의 두 정점 사이에 간선이 있는 지 없는 지 O(1)만에 판별
# 하지만 해당 정점의 이어진 모든 정점을 탐색하려면 한 줄의 배열을 전부 탐색하는 비효율적인면이 있습니다.

# 인접리스트방식의 장점은 어떤 정점에서 이어진 모든정점을 접근하는 속도가 빠릅니다.
# 굳이 모든 노드를 탐색할 필요없이 필요한 정점데이터만 가지고 있으므로 가능한 경우입니다.
# 한 정점과 연결된 모든 정점을 찾는 데 걸리는 시간 복잡도(효율성) : O(E) (정점의 차수)
# 다만 특정 정점에서 이어진 특정 정점의 데이터를 찾으려면 선형검색의 시간복잡도를 가지므로 비효율적입니다.

# 각 그래프구현방식에 대한 내용은 구글에 검색해보면 쉽게 나올겁니다.

# 그럼 둘 중 이 문제에 대한 어울리는 구현방식은 무엇일까요?
# 해당 문제는 완전탐색의 문제입니다. 1부터 시작해서 인접한 모든 정점을 어차피 한 번씩은 전부 봐야합니다.
# 그러므로 이 문제에서 가장 효율적인 방식은 인접리스트 방식입니다.
# ii.	BFS. 너비우선탐색
# A.	인접행렬 활용 구현
# i.	시간복잡도 : O(V^2)
# 1.	각 정점마다 bfs 1번씩 호출(V) * bfs 함수의 복잡도(V)
# B.	인접그래프 활용 구현
# i.	시간복잡도 : O(V+E) = O(E)  ( 보통 V<E )
# 1.	각 정점마다 bfs 1번씩 호출(V) + 각 정점과 연결된 간선을 검사하는데, 결국 모든 간선을 검사(E)

from collections import deque

def solution(n, vertex):
    answer = 0

    m=len(vertex)
    graph=[[] for _ in range(n+1)]
    for u,v in vertex:
        graph[v].append(u)
        graph[u].append(v)
    dist=[-1]*(n+1)

    s=1
    q=deque()
    q.append(s)
    dist[s]=0
    while q:
        now=q.popleft()
        for next in graph[now]:
            if dist[next]==-1:
                dist[next]=dist[now]+1
                q.append(next)

    max_val=0
    for a in dist:
        max_val=max(a,max_val)

    for i in dist:
        if i==max_val:
            answer+=1

    return answer

n=6
vertex=[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n,vertex))
