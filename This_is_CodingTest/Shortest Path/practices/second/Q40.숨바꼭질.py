import heapq

n,m=map(int,input().split())

INF=int(1e9)

start=1

graph=[[] for _ in range(n+1)]
distance=[INF]*(n+1)

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append((b,1))
    graph[b].append((a,1))

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0

    while q:
        dist,now=heapq.heappop(q)

        if distance[now]<dist:
            continue

        for i in graph[now]:
            cost=dist+i[1]

            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)
distance=distance[1:]

second=max(distance)
first=1e9
third=0
for i in range(len(distance)):
    if distance[i]==second:
        first=min(first,i+1)
        third+=1
print(first,second,third)