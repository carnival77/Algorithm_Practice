n,m = map(int,input().split())

# 북, 동, 남, 서
dx=[-1,0,1,0]
dy=[0,1,0,-1]

x,y,d=map(int,input().split()) # 현재 위치 및 방향
a=[list(map(int,input().split())) for _ in range(n)] # 청소하지 않은 빈 칸 : 0 , 벽 : 1 , 청소 완료 : 2
ans=0

while True:

    ok=False

    # 1. 현재 위치한 칸을 청소한다.
    a[x][y]=2

    # 2. 현재 위치에서 다음을 반복하면서 인접한 칸을 탐색한다
    for k in range(4):
        # 2.a. 현재 위치의 바로 왼쪽에 아직 청소하지 않은 빈 공간이 존재한다면, 왼쪽 방향으로 회전한 다음 한 칸을 전진하고 1번으로 돌아간다. 그렇지 않을 경우, 왼쪽 방향으로 회전한다.
        d = (d + 3) % 4
        nx, ny = x + dx[d], y + dy[d]
        if 0<=nx<n and 0<=ny<m and a[nx][ny] == 0:
            x, y = nx, ny
            ok=True
            break

    # 1번으로 돌아간다.
    if ok:
        continue

    # 2.b. 1번으로 돌아가거나 후진하지 않고 2a번 단계가 연속으로 네 번 실행되었을 경우, 바로 뒤쪽이 벽이라면 작동을 멈춘다. 그렇지 않다면 한 칸 후진한다.
    nx,ny = x-dx[d],y-dy[d]
    if a[nx][ny]==1:
        break
    else:
        x,y=nx,ny

for i in range(n):
    for j in range(m):
        if a[i][j]==2:
            ans+=1
print(ans)