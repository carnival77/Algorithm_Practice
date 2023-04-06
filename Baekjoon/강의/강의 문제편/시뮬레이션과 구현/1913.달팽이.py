import sys
input=sys.stdin.readline

n=int(input())
tg=int(input())
a=[[0]*n for _ in range(n)]
ans=None

# solution 1. 밖에서 안으로

# #  하,우,상,좌
dx=[1,0,-1,0]
dy=[0,1,0,-1]

x,y=0,0
d=0
a[x][y]=n**2

for v in range(n*n-1,0,-1):
    nx,ny=x+dx[d],y+dy[d]
    # 다음 칸이 범위 밖에 있거나 이미 값이 채워진 경우
    if not (0<=nx<n and 0<=ny<n) or a[nx][ny]!=0:
        # 방향 전환
        d=(d+1)%4
        # 전환된 방향의 전방 칸이 다음 칸
        nx, ny = x + dx[d], y + dy[d]
    a[nx][ny] = v
    if a[nx][ny]==tg:
        ans=[nx+1,ny+1]
    x, y = nx, ny

# solution 2. 안에서 밖으로

#    우,하,좌,상
dx = [0,1,0,-1]
dy = [1,0,-1,0]

x = (n-1)//2
y = (n-1)//2
# 가운데 칸 채우기
a[x][y] = 1
num = 2

# 각 레이어는 3~n 범위의 홀수들만큼의 변의 길이를 가진다.
for size in range(3, n+1, 2):
    # 다음 레이어로 갈 때 위로 한 칸
    x += dx[3]
    y += dy[3]
    # 값 채우기
    a[x][y] = num
    # 값 증가
    num += 1
    # 이번 레이어를 우,하,좌,상 순서로 탐색
    for k in range(4):
        # (size-1)만큼 loop를 돌며 값을 채울 텐데,
        loop = size - 1
        # 오른쪽 방향으로는 (loop-1)만큼 loop를 돈다.
        if k == 0:
            loop -= 1
        # 해당 loop 만큼 이동하며 값을 채운 후 값을 증가시킨다.
        for i in range(loop):
            x += dx[k]
            y += dy[k]
            a[x][y] = num
            num += 1

x = 0
y = 0
for index, row in enumerate(a):
    print(' '.join(map(str,row)))
    if tg in row:
        x = index+1
        y = row.index(tg)+1
print(str(x) + " " + str(y))