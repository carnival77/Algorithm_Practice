# solution 1. 조합으로 벽이 있는 곳 한 개씩 철거 후 재설치하며 bfs 탐색. 시간 초과.
# 벽이 있는 곳의 위치를 walls 배열에 담고, walls를 for문을 돌며 각 벽을 하나씩 철거하고 bfs를 돌린 뒤 다시 설치한다. 이렇게 나온 최단거리와, 벽을 철거하지 않아도 되는 경우의 최단 거리 중 최솟값을 리턴한다.

# from collections import deque
#
# dx=[-1,1,0,0]
# dy=[0,0,-1,1]
#
# n,m=map(int,input().split())
#
# def bfs():
#     q=deque()
#     q.append((0,0))
#     dist=[[-1]*n for _ in range(n)]
#     dist[0][0]=1
#     while q:
#         x,y=q.popleft()
#         for k in range(4):
#             nx,ny=x+dx[k],y+dy[k]
#             if 0<=nx<n and 0<=ny<m and a[nx][ny]==0 and dist[nx][ny]==-1:
#                 q.append((nx,ny))
#                 dist[nx][ny]=dist[x][y]+1
#     result=dist[n-1][m-1]
#     if result==-1:
#         return 1e9
#     else:
#         return result
#
# ans=1e9
# a=[]
# walls=[]
#
# for i in range(n):
#     row = list(map(int,list(input())))
#     for j in range(len(row)):
#         if row[j]==1:
#             walls.append((i,j))
#     a.append(row)
#
# for x,y in walls:
#     # ans=min(ans,bfs())
#     a[x][y]=0
#     ans = min(ans, bfs())
#     a[x][y] = 1
#
# if ans==1e9:
#     print(-1)
# else:
#     print(ans)

# solution 2. 가능한 이동 경우의 수를 구분하고 dist 배열을 3차원 배열으로 만들어 z축에 탐색 중 벽을 허물고 이동했는지 여부를 표시한다.
# 가능한 이동의 경우의 수는 3가지다. (1) 빈칸->빈칸 : 항상 / (2) 빈칸->벽 : 한 번만 / (3) 벽->빈칸 : 항상
# dist 배열을 3차원 배열 [x][y][z]로 만들고, 이중 z를 0 또는 1로 설정하여, 0은 빈 칸만 방문하며 탐색했을 경우, 그리고 1은 벽을 허물고 탐색했을 경우로 설정한다.
# 그리고 bfs 탐색 중 빈 칸에서 벽으로 이동하는 경우는 한 번만 가능하게끔 한다.

from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

n,m=map(int,input().split())

ans=1e9
a=[]

for i in range(n):
    row = list(map(int,list(input())))
    a.append(row)

# dist 배열을 3차원 배열 [x][y][z]로 만들고, 이중 z를 0 또는 1로 설정하여, 0은 빈 칸만 방문하며 탐색했을 경우, 그리고 1은 벽을 허물고 탐색했을 경우로 설정한다.
# dist 배열은 해당 칸까지의 최단 거리를 저장하며, -1로 초기화되어 -1일 경우 아직 방문하지 않은 칸을 나타낸다.
d=[[[0]*2 for j in range(m)] for i in range(n)]
d[0][0][0]=1

q=deque()
q.append((0,0,0))

while q:
    x,y,z=q.popleft() # (x,y) = 현재 칸의 위치 / z = 현재 칸에 도달하기까지 빈 칸만 지났다면 0, 벽을 한 번 허물었다면 1
    for k in range(4):
        nx,ny=x+dx[k],y+dy[k]
        if not (0<=nx<n and 0<=ny<m):
            continue
        # 빈 칸 방문
        if a[nx][ny]==0 and d[nx][ny][z]==0:
            q.append((nx,ny,z))
            d[nx][ny][z]=d[x][y][z]+1
        # 벽인 곳 부수고 방문 ( 한 번만 ). 만약 현재 칸에 도달하기까지 벽을 허문 적이 있다면, z=1이고, 아래의 z==0 조건을 만족하지 못하여, 위의 빈 칸 방문 조건만 만족하여 빈 칸만 방문할 수 있다.
        if a[nx][ny]==1 and z==0 and d[nx][ny][z+1]==0:
            q.append((nx, ny, z+1))
            d[nx][ny][z+1] = d[x][y][z]+1

if d[n-1][m-1][0]!=0 and d[n-1][m-1][1]!=0:
    print(min(d[n-1][m-1][0],d[n-1][m-1][1]))
elif d[n-1][m-1][0]!=0:
    print(d[n-1][m-1][0])
elif d[n-1][m-1][1]!=0:
    print(d[n-1][m-1][1])
else:
    print(-1)