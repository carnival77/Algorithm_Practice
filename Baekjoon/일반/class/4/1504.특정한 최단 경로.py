# import heapq
#
# n,m=map(int,input().split())
#
# INF=int(1e9)
#
# graph=[[] for _ in range(n+1)]
#
# for i in range(m):
#     a,b,c=map(int,input().split())
#     graph[a].append((b,c))
#     graph[b].append((a,c))
#
# v1,v2=map(int,input().split())
#
# def dijkstra(start,end):
#     q=[]
#     distance = [INF] * (n + 1)
#     heapq.heappush(q,(0,start))
#     distance[start]=0
#
#     while q:
#         dist,now=heapq.heappop(q)
#
#         if distance[now]<dist:
#             continue
#
#         for near_node_num,near_node_cost in graph[now]:
#             cost=dist+near_node_cost
#             if cost<distance[near_node_num]:
#                 distance[near_node_num]=cost
#                 heapq.heappush(q,(cost,near_node_num))
#
#     return distance[end]
#
# path1 = dijkstra(1,v1) + dijkstra(v1,v2) + dijkstra(v2,n)
# path2 = dijkstra(1,v2) + dijkstra(v2,v1) + dijkstra(v1,n)
#
# if path1>=INF and path2>=INF:
#     print(-1)
# else:
#     print(min(path1,path2))

INF = int(1e9) # 무한을 의미하는 10억으로 설정

# 노드, 간선 개수 입력
n,m = map(int,input().split())
# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신에게 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b]=0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a][b] = c
    graph[b][a] = c

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

v1,v2 = map(int,input().split())

path1=graph[1][v1] + graph[v1][v2] + graph[v2][n]
path2=graph[1][v2] + graph[v2][v1] + graph[v1][n]

# 수행된 결과 출력
if path1 >= INF and path2>=INF:
    print(-1)
else:
    print(min(path1,path2))