import sys
from collections import deque

m,n = map(int,input().split())

a=[]

dx=[-1,1,0,0]
dy=[0,0,-1,1]
ans=0

for _ in range(n):
    a.append(list(map(int,input().split())))

# 안 익은 토마토(0) 없이 모두 익어 있는 상태라면 0 출력
ok=False
for i in range(n):
    for j in range(m):
        if a[i][j] == 0:
            ok = True
if not ok:
    print(0)
    sys.exit(0)

q=deque()
# 최단 거리 구하기 위한 거리 배열 d. 그 중 익은 토마토(1)가 있는 지점은 시작 지점이므로 거리를 0으로 변환
# 큐에 그 시작 지점들을 넣기
d=[[-1]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if a[i][j]==1:
            d[i][j] = 0
            q.append((i,j))

while q:
    x,y = q.popleft()
    for dir in range(4):
        nx,ny = x+dx[dir],y+dy[dir]
        if 0<=nx<n and 0<=ny<m:
            # 만약 다음 칸의 요소가 0이고, 아직 방문하지 않아서 d의 요소가 -1일 경우
            if a[nx][ny] == 0 and d[nx][ny] == -1:
                a[nx][ny] = 1
                q.append((nx,ny))
                d[nx][ny] = d[x][y]+1

for i in range(n):
    for j in range(m):
        if a[i][j] == 0:
            print(-1)
            sys.exit(0)

# 최단 시간을 담은 d에서 가장 오래 걸린 시간이, 모든 칸의 토마토가 익기까지 걸린 시간
ans = max([max(row) for row in d])
print(ans)