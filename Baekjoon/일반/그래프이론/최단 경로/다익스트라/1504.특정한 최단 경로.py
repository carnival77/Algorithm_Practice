import heapq

n,m=map(int,input().split())

INF=int(1e9)

graph=[[] for _ in range(n+1)]

for i in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

v1,v2=map(int,input().split())

def dijkstra(start,end):
    q=[]
    distance = [INF] * (n + 1)
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

    return distance[end]

path1 = dijkstra(1,v1) + dijkstra(v1,v2) + dijkstra(v2,n)
path2 = dijkstra(1,v2) + dijkstra(v2,v1) + dijkstra(v1,n)

if path1>=INF and path2>=INF:
    print(-1)
else:
    print(min(path1,path2))