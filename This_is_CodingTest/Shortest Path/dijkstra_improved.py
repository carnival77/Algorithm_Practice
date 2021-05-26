import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억 설정

# 노드, 간선 개수 입력
n,m = map(int,input().split())
# 시작 노드 번호 입력
start = int(input())
# 각 노드별 연결 정보 리스트 입력
graph = [[] for i in range(n+1)]
# 방문 체크 리스트
visited = [False] * (n+1)
# 최단 거리 테이블. 초기값은 모두 무한
distance = [INF] * (n+1)

# 모든 간선 정보 입력
for _ in range(m):
    a,b,c = map(int,input().split())
    # a 번 노드에서 b 번 노드로 가는 비용이 c
    graph[a].append((b,c))

# 다익스트라 알고리즘
def dijkstra(start):
    q=[]

    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q,(0,start))
    distance[start]=0

    while q: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)

        # 현재 노드가 이미 처리된 노드라면 무시
        if distance[now] < dist:
            continue

        # 현재 노드와 연결된 다른 인접 노드를 확인
        for i in graph[now]:
            cost = dist + i[1]

            # 현재 노드를 거쳐 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

# start 번호의 노드부터 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1,n+1):
    # 도달할 수 없는 경우, 무한(INF)이라고 출력
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
