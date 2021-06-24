import heapq
import sys
input = sys.stdin.readline

INF = int(1e9) # 무한을 의미하는 값으로 10억 설정

n,m = map(int,input().split()) # 노드, 간선의 개수 입력 받기
start = int(input()) # 시작 노드 번호 입력받기
graph = [[] for i in range(n+1)] # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
distance = [INF] * (n+1) # 최단 거리 테이블을 모두 무한으로 초기화

# 모든 간선 정보 입력 받기
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q=[]
    # 시작 노드로 가기위 한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q,(0,start)) # 리스트, ( 거리, 노드 ) 를 heapq에 삽입
    distance[start] = 0
    while q: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 해당 노드까지 가는 최단 거리가 dist라는 정보에 대해, 해당 노드가 이미 처리된 적이 있어 이미 최단 거리 테이블에 최단 거리인 distance[now]가
        # 입력되어 있고 이것이 dist 현재의 해당 노드까지의 거리인 dist 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for near_nodes in graph[now]:
            cost = dist + near_nodes[1] # dist = 현 노드까지의 최단 거리. cost = 현 노드까지의 최단 거리 + 인접 노드까지의 거리
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[near_nodes[0]]:
                distance[near_nodes[0]] = cost # 최단 거리 테이블에서 해당 노드까지 가는 값을 cost 로 갱신한다
                heapq.heappush(q,(cost,near_nodes[0])) # 우선순위 큐에 인접 노드까지의 최단 거리와 인접 노드 번호를 삽입


dijkstra(start) # 시작점을 넣고 다익스트라 알고리즘 수행

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1,n+1):
    # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
    if distance[i] == INF:
        print("INFINITY")
    # 도달할 수 있는 경우 거리를 출력
    else:
        print(distance[i])

