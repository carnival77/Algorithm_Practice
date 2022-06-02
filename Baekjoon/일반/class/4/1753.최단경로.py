import heapq

n,m=map(int,input().split())
k=int(input())

INF=int(1e9)

graph=[[] for _ in range(n+1)]

for i in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))

distance=[INF]*(n+1)

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0

    while q:
        dist,now=heapq.heappop(q)

        if distance[now]<dist:
            continue

        for near_node_num,near_node_cost in graph[now]:
            cost=dist+near_node_cost
            if cost<distance[near_node_num]:
                distance[near_node_num]=cost
                heapq.heappush(q,(cost,near_node_num))

dijkstra(k)

for i in distance[1:]:
    if i==INF:
        print("INF")
    else:
        print(i)