from collections import deque

# 총 K번만 말과 같이 움직일 수 있고, 그 외에는 그냥 인접한 칸으로만 움직일 수 있다
dx = [0,0,1,-1,-2,-1,1,2,2,1,-1,-2]
dy = [1,-1,0,0,1,2,2,1,-1,-2,-2,-1]
cost = [0,0,0,0,1,1,1,1,1,1,1,1]

l=int(input())
m,n=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)]
# dist 배열을 3차원 배열 [x][y][z]로 만들고, 이중 z를 0<=z<=k로 설정하여, 0은 빈 칸만 방문하며 탐색했을 경우, 그리고 그 외의 수는, 그 수만큼 말의 이동법을 쓰고 탐색했을 경우로 설정한다.
# dist 배열은 해당 칸까지의 최단 거리를 저장하며, -1일 경우 아직 방문하지 않은 칸을 나타낸다.
d=[[[-1]*31 for j in range(m)] for i in range(n)]
d[0][0][0] = 0

ans=1e9
q=deque()
q.append((0,0,0))

while q:
    x,y,z=q.popleft() # (x,y) = 현재 칸의 위치 / z = 현재까지 말의 이동법을 쓴 횟수
    for k in range(12):
        nx,ny,nc=x+dx[k],y+dy[k],z+cost[k]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        # 빈 칸 방문
        # 말의 이동법을 써서 방문 ( k번째까지 ).
        if a[nx][ny]==0 and nc<=l and d[nx][ny][nc]==-1:
            q.append((nx,ny,nc))
            d[nx][ny][nc]=d[x][y][z]+1

for z in range(l+1):
    if d[n-1][m-1][z]!=-1:
        ans=min(ans,d[n-1][m-1][z])
if ans==1e9:
    print(-1)
else:
    print(ans)