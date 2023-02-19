import sys,heapq

dx=[-1,1,0,0]
dy=[0,0,1,-1]
INF=int(1e9)
index=1

def dijkstra(sx,sy):
    global n,matrix,distance
    q=[]
    distance = [[INF]*n for _ in range(n)]

    heapq.heappush(q,(matrix[0][0],sx,sy))
    distance[sx][sy]=matrix[0][0]

    while q:
        dist,cx,cy=heapq.heappop(q)

        if distance[cx][cy]<dist:
            continue

        for k in range(4):
            nx,ny=cx+dx[k],cy+dy[k]
            if 0<=nx<n and 0<=ny<n:
                near_node_cost=matrix[nx][ny]
                cost=dist+near_node_cost
                if cost<distance[nx][ny]:
                    distance[nx][ny]=cost
                    heapq.heappush(q,(cost,nx,ny))

while True:
    distance = []
    n=int(input())
    if n==0:
        sys.exit(0)

    matrix=[[0] * n for _ in range(n)]

    for i in range(n):
        row=list(map(int,input().split()))
        for j in range(n):
            matrix[i][j]=row[j]

    dijkstra(0,0)
    print("Problem",index,end='')
    print(":",distance[n-1][n-1])
    index+=1