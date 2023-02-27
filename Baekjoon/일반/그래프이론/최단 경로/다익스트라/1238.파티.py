import sys,heapq
input=sys.stdin.readline

n,m,x=map(int,input().split())
INF=int(1e9)
graph=[[] for _ in range(n+1)]
distance=[]

for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))

def dijkstra(start):
    global distance
    q=[]
    distance = [INF] * (n + 1)

    heapq.heappush(q,(0,start))
    distance[start]=0

    while q:
        dist,now=heapq.heappop(q)

        if distance[now]<dist:
            continue

        for near_node_num, near_node_cost in graph[now]:
            cost=dist+near_node_cost
            if cost<distance[near_node_num]:
                distance[near_node_num]=cost
                heapq.heappush(q,(cost,near_node_num))

dijkstra(x)
ans=distance

for i in range(1,n+1):
    dijkstra(i)
    ans[i]+=distance[x]

ans.pop(0)
ans.sort(reverse=True)
print(ans[0])