import heapq
import sys

input = sys.stdin.readline

n,m = map(int,input().split())
start = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

INF = int(1e9)

distance = [INF] * (n+1)

def dijstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)

        if dist > distance[now]:
            continue

        for near_node in graph[now]:
            cost = dist + near_node[1]
            if cost < distance[near_node[0]]:
                distance[near_node[0]] = cost
                heapq.heappush(q,(cost,near_node[0]))

dijstra(start)

for i in range(1,n+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])