from collections import deque

# 서, 북, 동, 남.
# 비트마스크로 벽 존재 여부를 체크해야 하므로, 위의 순서대로 0,1,2,3 으로 for문을 돌게 하여,
# 2^0=1, 2^1=2, 2^2=4, 2^3=8 값이 포함되어 있는지 & 연산으로 검사한다.
dx=[0,-1,0,1]
dy=[-1,0,1,0]

m,n=map(int,input().split())

a=[list(map(int,input().split())) for _ in range(n)]
d=[[-1]*m for _ in range(n)] # 영역별 번호를 넣는다. -1이면 아직 탐색되지 않은 칸
rooms=[] # 영역별 크기를 저장한다.
room_num=0

def bfs(sx,sy,room_num):
    cnt=1
    q=deque()
    q.append((sx,sy))
    d[sx][sy]=room_num

    while q:
        x,y=q.popleft()
        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]
            if 0<=nx<n and 0<=ny<m and d[nx][ny]==-1 and a[x][y] & (1<<k)==0:
                # 격자 범위 내이고, 미탐색되었으며, 현재 칸에서 해당 방향으로 벽이 없다면
                q.append((nx,ny))
                d[nx][ny]=room_num
                cnt+=1
    return cnt

# 1. 이 성에 있는 방의 개수
for i in range(n):
    for j in range(m):
        if d[i][j]==-1:
            rooms.append(bfs(i,j,room_num))
            room_num+=1
print(len(rooms))

# 2. 가장 넓은 방의 넓이
print(max(rooms))

# 3. 하나의 벽을 제거하여 얻을 수 있는 가장 넓은 방의 크기
ans=-1e9
for x in range(n):
    for y in range(m):
        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]
            if 0 <= nx < n and 0 <= ny < m and d[x][y]!=d[nx][ny] and a[x][y] & (1<<k)!=0:
                # 격자 범위 내이고, 탐색되었으며, 현재 칸에서 해당 방향으로 벽이 있다면
                ans=max(ans,rooms[d[x][y]]+rooms[d[nx][ny]])
print(ans)