import heapq
import sys

INF = int(1e9)

input = sys.stdin.readline

n,m = map(int,input().split())

graph = [[] for _ in range(n+1)]

start=1

for _ in range(m):
    a,b = map(int,input().split())
    c=1
    graph[a].append((b,c))
    graph[b].append((a,c))

def dijstra(start):
    distance = [INF] * (n + 1)
    q=[]
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        dist,now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for near_node_num,near_node_cost in graph[now]:
            cost = dist + near_node_cost
            if cost < distance[near_node_num]:
                distance[near_node_num]=cost
                heapq.heappush(q,(cost,near_node_num))

    return distance

distance = dijstra(start)[1:]

location_num=[]
location_distance=0
location_cnt=0

max_distance = max(distance)

for i in range(n):
    if distance[i] == max_distance:
        location_num.append(i)

min_location_num = min(location_num)+1
location_distance = distance[min_location_num]

for i in range(n):
    if location_distance == distance[i]:
        location_cnt += 1

print(min_location_num,location_distance,location_cnt)