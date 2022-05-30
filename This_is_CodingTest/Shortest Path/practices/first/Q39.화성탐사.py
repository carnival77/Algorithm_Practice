import heapq
import sys

input = sys.stdin.readline

INF = int(1e9)

dx = [-1,1,0,0]
dy = [0,0,1,-1]

T = int(input())

def dijstra(n,graph):
    distance = [[INF] * (n) for _ in range(n)]
    q=[]
    x,y=0,0
    distance[0][0] = graph[0][0]
    heapq.heappush(q,(graph[0][0],(0,0)))

    while q:
        dist,now = heapq.heappop(q)
        x,y = now

        if distance[x][y] < dist:
            continue

        for direction in range(4):
            nx = x + dx[direction]
            ny = y + dy[direction]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            cost = dist + graph[nx][ny]

            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q,(cost,(nx,ny)))

    return distance[n-1][n-1]

for i in range(T):
    n = int(input())
    graph = []

    for i in range(n):
        graph.append(list(map(int,input().split())))
    print(dijstra(n,graph))

