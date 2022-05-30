import heapq

INF=int(1e9)

dx=[-1,1,0,0]
dy=[0,0,-1,1]

t=int(input())
for _ in range(t):
    n=int(input())
    distance=[[INF]*(n) for _ in range(n)]

    graph=[list(map(int,input().split())) for _ in range(n)]

    q=[]

    heapq.heappush(q,(graph[0][0],[0,0]))
    distance[0][0]=graph[0][0]

    while q:
        dist,now=heapq.heappop(q)
        x,y=now

        if distance[x][y]<dist:
            continue

        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]
            if not (0<=nx<n and 0<=ny<n):
                continue
            cost=dist+graph[nx][ny]

            if cost<distance[nx][ny]:
                distance[nx][ny]=cost
                heapq.heappush(q,(cost,[nx,ny]))

    print(distance[n-1][n-1])