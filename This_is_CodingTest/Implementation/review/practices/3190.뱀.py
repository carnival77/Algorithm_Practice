from collections import deque

n=int(input())
k=int(input())

a=[[0] * n for i in range(n)]

# 사과가 있으면 1
for i in range(k):
    r,c = map(int,input().split())
    a[r-1][c-1]=1

l=int(input())
changes=dict()
for i in range(l):
    x,c = list(map(str,input().split()))
    # changes.append([int(x),c])
    changes[int(x)] = c

dx=[-1,0,1,0]
dy=[0,-1,0,1]

time=0
dir=3

# 머리 위치
x,y=0,0

# 뱀 정보
snake = deque()
snake.append((x,y))

while True:
    time +=1

    # 다음 칸
    nx = x + dx[dir]
    ny = y + dy[dir]

    # 벽 또는 자기 자신과 부딪히지 않으면
    if 0<=nx<n and 0<=ny<n and (nx,ny) not in snake:
        # 머리를 다음 칸에 위치
        snake.append((nx, ny))

        # 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
        if a[nx][ny] == 1:
            a[nx][ny] = 0
        # 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다.
        else:
            snake.popleft()
    else:
        break

    # 현재 칸으로 머리 위치 변경
    x,y = nx,ny

    # 초가 끝날 때 뱀의 방향 변환
    if time in changes.keys():
        c=changes[time]
        if c == 'L':
            dir = (dir+1)%4
        else:
            dir -= 1
            if dir < 0:
                dir=3
        del changes[time]

print(time)